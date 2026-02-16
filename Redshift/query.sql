-- Create Schema
CREATE SCHEMA IF NOT EXISTS airlines;

-- Create Dimension Table
CREATE TABLE airlines.airports_dim (
    airport_id BIGINT,
    city VARCHAR(100),
    state VARCHAR(100),
    name VARCHAR(200)
);

-- Load Data from S3
COPY airlines.airports_dim
FROM 's3://airline-landing-zn1/dim/airports.csv'
IAM_ROLE default
DELIMITER ','
IGNOREHEADER 1
REGION 'ap-south-1';


-----------------------------------------------------

-- Create Fact Table
CREATE TABLE airlines.daily_flights_fact (
    carrier VARCHAR(10),
    dep_airport VARCHAR(200),
    arr_airport VARCHAR(200),
    dep_city VARCHAR(100),
    arr_city VARCHAR(100),
    dep_state VARCHAR(100),
    arr_state VARCHAR(100),
    dep_delay BIGINT,
    arr_delay BIGINT
);
select * from  airlines.daily_flights_fact limit 3;
select * from airlines.airports_dim  limit 5;