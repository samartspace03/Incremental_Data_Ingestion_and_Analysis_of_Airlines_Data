import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# =====================================================
# READ DAILY FILES FROM GLUE CATALOG (S3 SOURCE)
# =====================================================
DailyFlights_node = glueContext.create_dynamic_frame.from_catalog(
    database="airline_datamart",
    table_name="daily_files",
    transformation_ctx="DailyFlights_node"
)

# =====================================================
# FILTER depdelay >= 60
# =====================================================
FilteredFlights_node = Filter.apply(
    frame=DailyFlights_node,
    f=lambda row: row["depdelay"] >= 60,
    transformation_ctx="FilteredFlights_node"
)

# =====================================================
# READ AIRPORT DIM FROM REDSHIFT
# =====================================================
AirportDim_node = glueContext.create_dynamic_frame.from_catalog(
    database="airline_datamart",
    table_name="imp_dbdev_airlines_airports_dim",
    redshift_tmp_dir="s3://resdshift-tmpdata1/airline_dim/",
    additional_options={
        "aws_iam_role": "arn:aws:iam::145689193771:role/service-role/AmazonRedshift-CommandsAccessRole-20260215T095113"
    },
    transformation_ctx="AirportDim_node"
)

# =====================================================
# JOIN FOR DEPARTURE DETAILS
# =====================================================
JoinDeparture_node = Join.apply(
    frame1=FilteredFlights_node,
    frame2=AirportDim_node,
    keys1=["originairportid"],      # ← KEEP ORIGINAL COLUMN NAME
    keys2=["airport_id"],
    transformation_ctx="JoinDeparture_node"
)

# =====================================================
# MAP DEPARTURE COLUMNS
# =====================================================
DepartureMapped_node = ApplyMapping.apply(
    frame=JoinDeparture_node,
    mappings=[
        ("carrier", "string", "carrier", "string"),
        ("destairportid", "long", "destairportid", "long"),
        ("depdelay", "long", "dep_delay", "long"),
        ("arrdelay", "long", "arr_delay", "long"),
        ("city", "string", "dep_city", "string"),
        ("name", "string", "dep_airport", "string"),
        ("state", "string", "dep_state", "string")
    ],
    transformation_ctx="DepartureMapped_node"
)

# =====================================================
# JOIN FOR ARRIVAL DETAILS
# =====================================================
JoinArrival_node = Join.apply(
    frame1=DepartureMapped_node,
    frame2=AirportDim_node,
    keys1=["destairportid"],        # ← KEEP ORIGINAL COLUMN NAME
    keys2=["airport_id"],
    transformation_ctx="JoinArrival_node"
)

# =====================================================
# MAP ARRIVAL COLUMNS
# =====================================================
Final_node = ApplyMapping.apply(
    frame=JoinArrival_node,
    mappings=[
        ("carrier", "string", "carrier", "string"),
        ("dep_delay", "long", "dep_delay", "long"),
        ("arr_delay", "long", "arr_delay", "long"),
        ("dep_city", "string", "dep_city", "string"),
        ("dep_airport", "string", "dep_airport", "string"),
        ("dep_state", "string", "dep_state", "string"),
        ("city", "string", "arr_city", "string"),
        ("name", "string", "arr_airport", "string"),
        ("state", "string", "arr_state", "string")
    ],
    transformation_ctx="Final_node"
)

# =====================================================
# WRITE TO REDSHIFT FACT TABLE
# =====================================================
glueContext.write_dynamic_frame.from_catalog(
    frame=Final_node,
    database="airline_datamart",
    table_name="db2dev_airlines_daily_flights_fact",
    redshift_tmp_dir="s3://resdshift-tmpdata1/airline-fact/",
    additional_options={
        "aws_iam_role": "arn:aws:iam::145689193771:role/service-role/AmazonRedshift-CommandsAccessRole-20260215T095113"
    },
    transformation_ctx="RedshiftTarget_node"
)

job.commit()
