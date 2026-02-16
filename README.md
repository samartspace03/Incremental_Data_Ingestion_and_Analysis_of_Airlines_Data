# ✈️ Airline Data Ingestion & Analytics Pipeline (AWS)

## 📌 Project Overview

This project demonstrates a **serverless, event-driven airline data ingestion pipeline** built using AWS services.  
The pipeline automatically ingests raw airline datasets, performs ETL transformations, loads them into a data warehouse, and enables analytics using a star schema model.

The solution is designed to simulate a **production-ready data engineering workflow** with orchestration, monitoring, and failure notifications.

---

## 🏗️ Architecture Overview

The pipeline follows an event-driven architecture:

- Raw airline data is uploaded to **Amazon S3**
- **Amazon EventBridge** detects the file upload event
- **AWS Step Functions** orchestrates the workflow
- **AWS Glue Crawler** updates the schema in the Data Catalog
- **AWS Glue Job** performs ETL transformations
- Transformed data is loaded into **Amazon Redshift**
- On failure, **Amazon SNS** sends notification alerts

---

## ⚙️ AWS Services Used

- **Amazon S3** – Data lake storage  
- **Amazon EventBridge** – Event trigger mechanism  
- **AWS Step Functions** – Workflow orchestration  
- **AWS Glue (Crawler + Job)** – Schema discovery & ETL  
- **Amazon Redshift** – Data warehouse  
- **Amazon SNS** – Failure notifications  

---

## 🔄 Workflow Execution

### 1️⃣ Data Ingestion
Raw airline CSV files (dimension & fact data) are uploaded into S3.

### 2️⃣ Event Trigger
EventBridge automatically triggers the Step Function workflow when a new file is added.

### 3️⃣ Schema Discovery
Glue Crawler scans S3 and updates the Glue Data Catalog.

### 4️⃣ ETL Processing
Glue Job:
- Cleans data  
- Handles NULL values  
- Applies column mapping  
- Transforms datasets  
- Writes processed data  

### 5️⃣ Data Warehouse Load
Processed data is loaded into Amazon Redshift using a star schema:

- `airport_dim` (Dimension Table)
- `flight_fact` (Fact Table)

### 6️⃣ Monitoring & Alerts
If the Glue job fails, SNS sends email notifications.

---

## 📊 Data Model (Star Schema)

### 🔹 Dimension Table: `airport_dim`

- airport_id  
- airport_name  
- city  
- state  

### 🔹 Fact Table: `flight_fact`

- flight_id  
- departure_airport_id  
- arrival_airport_id  
- delay  
- flight_date  

---

## 📁 Project Structure

airline-data-ingestion-pipeline/
│
├── README.md
├── architecture/ # Architecture diagrams & design explanation
├── glue/ # ETL scripts & crawler configs
├── step-functions/ # State machine definitions
├── eventbridge/ # Event rule configuration
├── redshift/ # SQL scripts for schema & queries
├── sns/ # Notification setup
├── sample-data/ # Sample CSV datasets
├── outputs/ # Execution outputs & results
└── docs/ # Setup guide & troubleshooting


---

## 🚀 How to Deploy

1. Create S3 bucket (raw + processed zones)  
2. Upload sample airline data  
3. Configure Glue Crawler  
4. Create Glue ETL Job  
5. Create Redshift tables  
6. Deploy Step Function state machine  
7. Configure EventBridge rule  
8. Configure SNS email subscription  
9. Upload new file to S3 to trigger pipeline  

---

## 🔍 Key Features

- Event-driven architecture  
- Serverless design  
- Automated schema discovery  
- Orchestrated ETL pipeline  
- Star schema modeling  
- Failure handling with alerts  
- Scalable and production-ready design  

---

## 📈 Sample Output

After successful execution:

- Transformed datasets stored in S3  
- Data loaded into Redshift  
- Step Function execution marked as **SUCCEEDED**  
- Analytics queries can be executed on fact & dimension tables  

---

## 🛠️ Future Improvements

- Add data validation framework  
- Implement incremental loading logic  
- Add CloudWatch monitoring dashboards  
- Use Terraform for Infrastructure as Code  
- Add CI/CD pipeline for deployment  
- Implement partitioning strategy in S3  

---

