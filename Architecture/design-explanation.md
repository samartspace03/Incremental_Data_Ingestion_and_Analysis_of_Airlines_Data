# 🏗️ Architecture Design Explanation

## 1. Overview

This project implements a serverless, event-driven airline data ingestion pipeline using AWS services.  
The system is designed to automatically process airline datasets from ingestion to analytics with monitoring and failure handling.

---

## 2. Architecture Design Pattern

The solution follows these architectural principles:

- Event-Driven Architecture
- Serverless Computing
- Orchestrated ETL Workflow
- Star Schema Data Modeling
- Automated Monitoring & Alerts

---

## 3. Component-Level Explanation

### 3.1 Amazon S3 (Data Lake)

S3 acts as the raw and processed data storage layer.

Zones:
- Raw Layer – Incoming airline CSV files
- Processed Layer – Transformed datasets

Benefits:
- Highly scalable
- Durable storage
- Cost-effective

---

### 3.2 Amazon EventBridge

EventBridge listens for object creation events in S3.

When a new file is uploaded:
- It triggers the Step Functions workflow
- No manual intervention required

This enables true event-driven automation.

---

### 3.3 AWS Step Functions (Orchestration Layer)

Step Functions manages the entire workflow:

1. Start Glue Crawler
2. Wait for crawler completion
3. Start Glue ETL Job
4. Handle success or failure
5. Trigger SNS notification if failure

Why orchestration?
- Centralized workflow management
- Built-in retry logic
- Visual monitoring of execution

---

### 3.4 AWS Glue Crawler

The crawler:
- Scans S3 raw data
- Infers schema
- Updates Glue Data Catalog

This ensures schema evolution is handled automatically.

---

### 3.5 AWS Glue Job (ETL Processing)

The Glue Job:
- Cleans and transforms data
- Handles NULL values
- Applies column mapping
- Writes processed data
- Loads data into Redshift

Built using PySpark.

---

### 3.6 Amazon Redshift (Data Warehouse)

Redshift stores processed data in a star schema:

- airport_dim (Dimension Table)
- flight_fact (Fact Table)

Enables:
- Fast analytics
- SQL querying
- BI tool integration

---

### 3.7 Amazon SNS (Monitoring & Alerts)

SNS sends email notifications when:
- Glue job fails
- Workflow errors occur

Ensures operational visibility.

---

## 4. Data Flow Summary

S3 → EventBridge → Step Functions → Glue Crawler → Glue Job → Redshift → SNS (on failure)

---

## 5. Scalability & Production Readiness

- Fully serverless
- Automatically scalable
- Fault-tolerant
- Monitored via workflow states
- Easily extendable for incremental loads

---

## 6. Design Decisions

- Used Step Functions for reliability and visual monitoring
- Used Glue Crawler for automated schema management
- Used Redshift for warehouse-style analytics
- Used SNS for lightweight failure alerting
