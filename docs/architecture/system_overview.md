# System Architecture Overview

## Components
- **Data Ingestion Layer**: Airflow DAGs for data collection
- **Staging Layer**: Raw data storage and initial transformations
- **Data Warehouse**: Structured data models (staging, marts, dimensions)
- **Analytics Layer**: DBT models for business intelligence

## Data Flow
1. Source Systems → Airflow DAGs
2. Airflow → Staging Tables
3. Staging → DBT Transformations
4. DBT → Data Marts & Dimensions
