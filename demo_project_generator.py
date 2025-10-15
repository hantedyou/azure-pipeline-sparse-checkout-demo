#!/usr/bin/env python3
"""
Azure DevOps Sparse Checkout Demo Project Generator
Generates a realistic financial data engineering project structure for sparse checkout demonstration
"""

import os
import json
import random
from pathlib import Path

def create_directory_structure():
    """Create the main directory structure"""
    directories = [
        "dags",
        "metadata/schemas",
        "metadata/configs",
        "data_model/staging",
        "data_model/marts",
        "data_model/dimensions",
        "data_model/migrations",
        "dbt/models/staging",
        "dbt/models/marts",
        "dbt/models/dimensions",
        "dbt/models/metrics",
        "dbt/macros",
        "dbt/tests/generic",
        "dbt/tests/singular",
        "dbt/snapshots",
        "deployment",
        "deployment/terraform",
        "deployment/kubernetes",
        "utils",
        "utils/data_quality",
        "utils/monitoring",
        "utils/connectors",
        "docs",
        "docs/architecture",
        "docs/runbooks",
        "sample_data",
        "scripts",
        "config/prod",
        "config/staging",
        "config/dev"
    ]

    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
    print(f"✅ Created {len(directories)} directories")

def generate_dag_files():
    """Generate 60+ DAG files for financial data pipelines"""
    dag_templates = [
        # Market Data (15)
        "stock_price_ingestion", "bond_yield_analysis", "forex_rates_pipeline",
        "commodity_prices_etl", "crypto_market_data", "options_chain_ingestion",
        "futures_contracts_etl", "market_indices_pipeline", "earnings_data_ingestion",
        "dividend_announcements_etl", "stock_splits_pipeline", "ipo_data_ingestion",
        "market_sentiment_analysis", "technical_indicators_pipeline", "analyst_ratings_etl",

        # Trading & Risk (15)
        "trade_settlement_pipeline", "risk_exposure_calculation", "portfolio_valuation_etl",
        "margin_requirements_analysis", "credit_risk_assessment", "market_risk_pipeline",
        "liquidity_risk_analysis", "operational_risk_etl", "counterparty_risk_pipeline",
        "var_calculation_pipeline", "stress_testing_pipeline", "collateral_management_etl",
        "position_reconciliation", "trade_confirmation_pipeline", "netting_calculation_etl",

        # Regulatory & Compliance (12)
        "regulatory_reporting_pipeline", "compliance_monitoring_etl", "audit_trail_ingestion",
        "kyc_data_pipeline", "aml_transaction_monitoring", "sanctions_screening_pipeline",
        "mifid_reporting_etl", "emir_reporting_pipeline", "dodd_frank_reporting",
        "basel_iii_calculations", "solvency_reporting_etl", "fatca_crs_reporting",

        # Reference Data (10)
        "security_master_sync", "counterparty_master_etl", "currency_reference_data",
        "exchange_calendar_sync", "corporate_actions_pipeline", "issuer_master_etl",
        "market_data_vendor_sync", "holiday_calendar_update", "instrument_classification_etl",
        "legal_entity_identifier_sync",

        # Analytics & Reporting (8)
        "daily_pnl_calculation", "mtm_valuation_pipeline", "performance_attribution_etl",
        "risk_dashboard_refresh", "executive_summary_pipeline", "client_reporting_etl",
        "benchmark_comparison_pipeline", "portfolio_analytics_refresh",

        # Data Quality & Monitoring (5)
        "data_quality_checks_pipeline", "reconciliation_pipeline", "data_lineage_tracking",
        "anomaly_detection_pipeline", "sla_monitoring_etl"
    ]
    
    dag_template = '''"""
{dag_name} DAG for financial data processing
Generated for Azure DevOps Sparse Checkout Demo
"""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator

default_args = {{
    'owner': 'data_engineering_team',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5)
}}

dag = DAG(
    '{dag_id}',
    default_args=default_args,
    description='{description}',
    schedule_interval='@daily',
    catchup=False,
    tags=['{tag1}', '{tag2}']
)

def extract_data():
    """Extract data from source systems"""
    print("Extracting {data_type} data...")
    # Demo: Simulate data extraction
    pass

def transform_data():
    """Transform and validate data"""
    print("Transforming {data_type} data...")
    # Demo: Simulate data transformation
    pass

def load_data():
    """Load data to target warehouse"""
    print("Loading {data_type} data to warehouse...")
    # Demo: Simulate data loading
    pass

# Define tasks
extract_task = PythonOperator(
    task_id='extract_{task_suffix}',
    python_callable=extract_data,
    dag=dag
)

transform_task = PythonOperator(
    task_id='transform_{task_suffix}',
    python_callable=transform_data,
    dag=dag
)

load_task = PythonOperator(
    task_id='load_{task_suffix}',
    python_callable=load_data,
    dag=dag
)

# Task dependencies
extract_task >> transform_task >> load_task
'''

    for i, dag_name in enumerate(dag_templates):
        tags = random.sample(['market_data', 'trading', 'risk', 'compliance', 'reporting', 'real_time'], 2)
        
        content = dag_template.format(
            dag_name=dag_name.replace('_', ' ').title(),
            dag_id=dag_name,
            description=f"Process {dag_name.replace('_', ' ')} for financial analysis",
            tag1=tags[0],
            tag2=tags[1],
            data_type=dag_name.split('_')[0],
            task_suffix=dag_name.split('_')[0]
        )
        
        with open(f"dags/{dag_name}.py", "w") as f:
            f.write(content)
    
    print(f"✅ Generated {len(dag_templates)} DAG files")

def generate_metadata_files():
    """Generate metadata and configuration files"""

    # Schema files - expanded to 25+ schemas
    schemas = [
        # Market Data
        "stock_price_schema.json", "bond_yield_schema.json", "forex_rates_schema.json",
        "options_chain_schema.json", "futures_contracts_schema.json", "crypto_prices_schema.json",
        "commodity_prices_schema.json", "market_indices_schema.json", "earnings_schema.json",

        # Trading
        "trade_settlement_schema.json", "trade_confirmation_schema.json", "order_book_schema.json",
        "execution_reports_schema.json", "position_schema.json",

        # Risk
        "risk_exposure_schema.json", "var_metrics_schema.json", "stress_test_schema.json",
        "collateral_schema.json", "margin_calls_schema.json",

        # Reference Data
        "portfolio_schema.json", "security_master_schema.json", "counterparty_schema.json",
        "currency_reference_schema.json", "exchange_calendar_schema.json",

        # Compliance
        "kyc_schema.json", "aml_alerts_schema.json", "regulatory_report_schema.json"
    ]
    
    schema_template = {
        "table_name": "{table}",
        "schema": "staging",
        "columns": [
            {"name": "id", "type": "BIGINT", "nullable": False, "primary_key": True},
            {"name": "symbol", "type": "VARCHAR(10)", "nullable": False},
            {"name": "price", "type": "DECIMAL(18,6)", "nullable": True},
            {"name": "volume", "type": "BIGINT", "nullable": True},
            {"name": "timestamp", "type": "TIMESTAMP", "nullable": False},
            {"name": "created_at", "type": "TIMESTAMP", "nullable": False}
        ],
        "partitions": ["DATE(timestamp)"],
        "indexes": ["symbol", "timestamp"]
    }
    
    for schema in schemas:
        table_name = schema.replace('_schema.json', '')
        schema_content = schema_template.copy()
        schema_content["table_name"] = table_name
        
        with open(f"metadata/schemas/{schema}", "w") as f:
            json.dump(schema_content, f, indent=2)
    
    # Config files - expanded to 15+ configs
    configs = [
        "database_connections.yaml", "data_quality_rules.yaml", "monitoring_config.yaml",
        "alerting_rules.yaml", "sla_definitions.yaml", "retention_policies.yaml",
        "encryption_config.yaml", "access_control.yaml", "rate_limits.yaml",
        "backup_schedule.yaml", "disaster_recovery.yaml", "audit_logging.yaml",
        "api_endpoints.yaml", "vendor_connections.yaml", "notification_channels.yaml"
    ]
    
    config_template = '''# {config_name} Configuration
# Generated for Azure DevOps Sparse Checkout Demo

production:
  host: prod-db.company.com
  port: 5432
  database: financial_dw
  schema: {schema}
  
staging:
  host: staging-db.company.com  
  port: 5432
  database: financial_dw_staging
  schema: {schema}

development:
  host: dev-db.company.com
  port: 5432
  database: financial_dw_dev
  schema: {schema}
'''

    for config in configs:
        content = config_template.format(
            config_name=config.replace('.yaml', '').replace('_', ' ').title(),
            schema=config.split('_')[0]
        )
        with open(f"metadata/configs/{config}", "w") as f:
            f.write(content)
    
    print(f"✅ Generated {len(schemas)} schema files and {len(configs)} config files")

def generate_data_model_files():
    """Generate DDL files for different layers"""

    # Staging DDLs - expanded to 25+ tables
    staging_tables = [
        # Market Data
        "stg_stock_prices", "stg_bond_yields", "stg_forex_rates", "stg_options_chain",
        "stg_futures_contracts", "stg_crypto_prices", "stg_commodity_prices",
        "stg_market_indices", "stg_earnings_data", "stg_dividends",

        # Trading
        "stg_trade_settlements", "stg_trade_confirmations", "stg_order_book",
        "stg_execution_reports", "stg_positions",

        # Risk
        "stg_risk_exposures", "stg_var_metrics", "stg_stress_tests",
        "stg_collateral", "stg_margin_calls",

        # Reference Data
        "stg_security_master", "stg_counterparties", "stg_currencies",
        "stg_exchange_calendars", "stg_corporate_actions"
    ]
    
    ddl_template = '''-- {table_name} DDL
-- Generated for Azure DevOps Sparse Checkout Demo

CREATE TABLE IF NOT EXISTS {schema}.{table_name} (
    id BIGINT IDENTITY(1,1) PRIMARY KEY,
    symbol VARCHAR(10) NOT NULL,
    price DECIMAL(18,6),
    volume BIGINT,
    timestamp TIMESTAMP NOT NULL,
    source_system VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes
CREATE INDEX idx_{table_name}_symbol ON {schema}.{table_name}(symbol);
CREATE INDEX idx_{table_name}_timestamp ON {schema}.{table_name}(timestamp);

-- Partitioning
ALTER TABLE {schema}.{table_name} 
PARTITION BY RANGE (DATE(timestamp));

-- Comments
COMMENT ON TABLE {schema}.{table_name} IS '{description}';
'''

    for table in staging_tables:
        content = ddl_template.format(
            table_name=table,
            schema='staging',
            description=f'Staging table for {table.replace("stg_", "").replace("_", " ")}'
        )
        with open(f"data_model/staging/{table}.sql", "w") as f:
            f.write(content)
    
    # Marts DDLs - expanded to 20+ tables
    marts_tables = [
        # Facts
        "fact_trades", "fact_positions", "fact_pnl", "fact_risk_metrics",
        "fact_market_data", "fact_settlements", "fact_executions",

        # Aggregates
        "agg_daily_trading_volume", "agg_portfolio_performance", "agg_risk_summary",
        "agg_market_statistics", "agg_compliance_metrics"
    ]

    for table in marts_tables:
        content = ddl_template.format(
            table_name=table,
            schema='marts',
            description=f'Data mart table for {table.replace("_", " ")}'
        )
        with open(f"data_model/marts/{table}.sql", "w") as f:
            f.write(content)

    # Dimension DDLs - new section
    dimension_tables = [
        "dim_securities", "dim_counterparties", "dim_accounts", "dim_traders",
        "dim_products", "dim_exchanges", "dim_currencies", "dim_dates"
    ]

    for table in dimension_tables:
        content = ddl_template.format(
            table_name=table,
            schema='dimensions',
            description=f'Dimension table for {table.replace("dim_", "").replace("_", " ")}'
        )
        with open(f"data_model/dimensions/{table}.sql", "w") as f:
            f.write(content)

    print(f"✅ Generated {len(staging_tables + marts_tables + dimension_tables)} DDL files")

def generate_dbt_files():
    """Generate DBT models and SQL files"""

    # Staging models - expanded to match data model
    staging_models = [
        "stg_stock_prices", "stg_bond_yields", "stg_forex_rates", "stg_options_chain",
        "stg_futures_contracts", "stg_crypto_prices", "stg_commodity_prices",
        "stg_trade_settlements", "stg_trade_confirmations", "stg_risk_exposures",
        "stg_var_metrics", "stg_security_master", "stg_counterparties"
    ]
    
    staging_template = '''{{{{
  config(
    materialized='view',
    schema='staging'
  )
}}}}

-- {model_name} staging model
-- Generated for Azure DevOps Sparse Checkout Demo

SELECT
    id,
    symbol,
    CAST(price AS DECIMAL(18,6)) AS price,
    volume,
    timestamp,
    source_system,
    created_at,
    updated_at
FROM {{{{ source('raw', '{source_table}') }}}}
WHERE timestamp >= CURRENT_DATE - INTERVAL '7 days'
  AND price IS NOT NULL
  AND symbol IS NOT NULL
'''

    for model in staging_models:
        content = staging_template.format(
            model_name=model,
            source_table=model.replace('stg_', 'raw_')
        )
        with open(f"dbt/models/staging/{model}.sql", "w") as f:
            f.write(content)
    
    # Mart models - expanded
    marts_models = [
        "fact_daily_prices", "fact_trade_summary", "fact_pnl_daily",
        "fact_risk_metrics_daily", "agg_portfolio_performance", "agg_market_statistics"
    ]

    mart_template = '''{{{{
  config(
    materialized='table',
    schema='marts',
    indexes=[
      {{'columns': ['symbol'], 'type': 'btree'}},
      {{'columns': ['date'], 'type': 'btree'}}
    ]
  )
}}}}

-- {model_name} mart model
-- Generated for Azure DevOps Sparse Checkout Demo

SELECT
    symbol,
    date,
    AVG(price) AS avg_price,
    MIN(price) AS min_price,
    MAX(price) AS max_price,
    SUM(volume) AS total_volume,
    COUNT(*) AS trade_count,
    CURRENT_TIMESTAMP AS created_at
FROM {{{{ ref('stg_stock_prices') }}}}
WHERE date >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY symbol, date
'''

    for model in marts_models:
        content = mart_template.format(model_name=model)
        with open(f"dbt/models/marts/{model}.sql", "w") as f:
            f.write(content)

    # Dimension models
    dimension_models = [
        "dim_securities", "dim_counterparties", "dim_traders", "dim_products"
    ]

    dim_template = '''{{{{
  config(
    materialized='table',
    schema='dimensions'
  )
}}}}

-- {model_name} dimension model
SELECT DISTINCT
    id,
    name,
    type,
    created_at,
    updated_at
FROM {{{{ ref('stg_security_master') }}}}
'''

    for model in dimension_models:
        content = dim_template.format(model_name=model)
        with open(f"dbt/models/dimensions/{model}.sql", "w") as f:
            f.write(content)

    # DBT macros - expanded
    macros = {
        "financial_calculations.sql": '''-- Financial calculation macros
{% macro calculate_returns(price_column, periods=1) %}
  ({{ price_column }} - LAG({{ price_column }}, {{ periods }}) OVER (ORDER BY timestamp))
  / LAG({{ price_column }}, {{ periods }}) OVER (ORDER BY timestamp) * 100
{% endmacro %}

{% macro calculate_sharpe_ratio(returns, risk_free_rate=0.02) %}
  (AVG({{ returns }}) - {{ risk_free_rate }}) / STDDEV({{ returns }})
{% endmacro %}
''',
        "data_quality.sql": '''-- Data quality macros
{% macro check_null_values(column_name) %}
  COUNT(CASE WHEN {{ column_name }} IS NULL THEN 1 END)
{% endmacro %}

{% macro check_duplicates(columns) %}
  COUNT(*) - COUNT(DISTINCT {{ columns }})
{% endmacro %}
''',
        "date_utils.sql": '''-- Date utility macros
{% macro get_business_days(start_date, end_date) %}
  SELECT COUNT(*) FROM dim_dates
  WHERE date BETWEEN {{ start_date }} AND {{ end_date }}
  AND is_business_day = TRUE
{% endmacro %}
'''
    }

    for filename, content in macros.items():
        with open(f"dbt/macros/{filename}", "w") as f:
            f.write(content)

    # DBT tests - generic
    test_content = '''version: 2

sources:
  - name: raw
    tables:
      - name: raw_stock_prices
        columns:
          - name: id
            tests:
              - unique
              - not_null
'''
    with open("dbt/tests/generic/source_tests.yml", "w") as f:
        f.write(test_content)

    # DBT tests - singular
    singular_tests = ["test_price_anomalies.sql", "test_volume_spikes.sql", "test_missing_dates.sql"]
    for test in singular_tests:
        test_sql = f'''-- {test.replace('.sql', '').replace('_', ' ').title()}
SELECT * FROM {{{{ ref('stg_stock_prices') }}}}
WHERE price < 0 OR price > 1000000
'''
        with open(f"dbt/tests/singular/{test}", "w") as f:
            f.write(test_sql)

    print(f"✅ Generated {len(staging_models + marts_models + dimension_models)} DBT models, {len(macros)} macros, and {len(singular_tests)} tests")

def generate_deployment_files():
    """Generate deployment configuration and sample deploy list"""
    
    # Sample deployment list
    deploy_list = '''# Deployment List for Sparse Checkout Demo
# Format: one file path per line
# This list simulates a partial deployment

dags/stock_price_ingestion.py
dags/bond_yield_analysis.py
dags/forex_rates_pipeline.py
metadata/schemas/stock_price_schema.json
metadata/schemas/bond_yield_schema.json
data_model/staging/stg_stock_prices.sql
data_model/staging/stg_bond_yields.sql
dbt/models/staging/stg_stock_prices.sql
dbt/models/staging/stg_bond_yields.sql
dbt/models/marts/fact_daily_prices.sql
'''
    
    with open("deployment/deploy-list.txt", "w") as f:
        f.write(deploy_list)
    
    # Azure DevOps variable template
    variables_content = '''# Azure DevOps Variables Template
# Generated for Sparse Checkout Demo

variables:
  - name: 'shallow_fetch_depth'
    value: '5'
  - name: 'target_environment' 
    value: 'staging'
  - name: 'deployment_path'
    value: '/opt/financial-pipeline'
  - name: 'artifact_name'
    value: 'financial-pipeline-$(Build.BuildNumber)'
'''
    
    with open("deployment/pipeline-variables.yml", "w") as f:
        f.write(variables_content)
    
    print("✅ Generated deployment configuration files")

def generate_utility_files():
    """Generate utility scripts and documentation"""
    
    # Utility script
    util_content = '''#!/usr/bin/env python3
"""
Utility functions for financial data pipeline
Generated for Azure DevOps Sparse Checkout Demo
"""

import logging
import pandas as pd
from datetime import datetime

def setup_logging():
    """Setup logging configuration"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

def validate_financial_data(df: pd.DataFrame) -> bool:
    """Validate financial data quality"""
    required_columns = ['symbol', 'price', 'timestamp']
    
    if not all(col in df.columns for col in required_columns):
        return False
    
    if df['price'].isnull().any():
        return False
        
    return True

def calculate_market_cap(price: float, shares_outstanding: int) -> float:
    """Calculate market capitalization"""
    return price * shares_outstanding

class FinancialDataProcessor:
    """Financial data processing utilities"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def process_stock_data(self, data):
        """Process stock price data"""
        self.logger.info("Processing stock data...")
        # Demo implementation
        return data
    
    def calculate_volatility(self, prices):
        """Calculate price volatility"""
        return prices.std() / prices.mean()
'''
    
    with open("utils/financial_utils.py", "w") as f:
        f.write(util_content)
    
    # Documentation
    readme_content = '''# Financial Data Pipeline Demo

This project demonstrates Azure DevOps sparse checkout optimization for large-scale data engineering projects.

## Project Structure

```
├── dags/                    # Airflow DAG definitions (20 files)
├── metadata/               # Data schemas and configurations
│   ├── schemas/           # JSON schema definitions
│   └── configs/           # YAML configuration files
├── data_model/            # Database DDL definitions
│   ├── staging/          # Staging layer tables
│   ├── marts/            # Data mart tables
│   └── dimensions/       # Dimension tables
├── dbt/                   # DBT models and transformations
│   ├── models/           # SQL models
│   ├── macros/           # Reusable macros
│   └── tests/            # Data quality tests
├── deployment/           # CI/CD configuration
├── utils/                # Utility functions
└── docs/                 # Documentation
```

## Sparse Checkout Demo

This project simulates a real financial data engineering environment with:
- 20+ Airflow DAGs for different financial data pipelines
- Metadata schemas for various financial instruments
- DDL files for staging and mart layers
- DBT models for data transformation
- Utility functions for data processing

The deployment list in `deployment/deploy-list.txt` shows how sparse checkout can dramatically reduce deployment time by only checking out necessary files.

## Azure DevOps Integration

Use the provided YAML configuration to demonstrate:
1. Shallow fetch (--depth 5)
2. Sparse checkout configuration
3. Selective file deployment
4. Performance optimization

Generated for Azure DevOps Sparse Checkout demonstration.
'''
    
    with open("README.md", "w") as f:
        f.write(readme_content)
    
    print("✅ Generated utility files and documentation")

def generate_utility_scripts():
    """Generate additional utility scripts"""

    utils_scripts = {
        "utils/data_quality/validator.py": '''"""Data quality validation utilities"""
import pandas as pd
from typing import Dict, List

class DataValidator:
    def validate_schema(self, df: pd.DataFrame, expected_schema: Dict) -> bool:
        """Validate dataframe schema"""
        return all(col in df.columns for col in expected_schema.keys())

    def check_null_percentage(self, df: pd.DataFrame, threshold: float = 0.1) -> Dict:
        """Check null percentage for each column"""
        return {col: df[col].isnull().mean() for col in df.columns}
''',
        "utils/data_quality/anomaly_detector.py": '''"""Anomaly detection for financial data"""
import numpy as np

class AnomalyDetector:
    def detect_outliers(self, data, method='iqr'):
        """Detect outliers using IQR or Z-score"""
        if method == 'iqr':
            Q1 = np.percentile(data, 25)
            Q3 = np.percentile(data, 75)
            IQR = Q3 - Q1
            return (data < Q1 - 1.5 * IQR) | (data > Q3 + 1.5 * IQR)
''',
        "utils/monitoring/metrics_collector.py": '''"""Metrics collection for monitoring"""
import time
from datetime import datetime

class MetricsCollector:
    def __init__(self):
        self.metrics = {}

    def record_metric(self, name: str, value: float):
        """Record a metric value"""
        self.metrics[name] = {
            'value': value,
            'timestamp': datetime.now()
        }
''',
        "utils/monitoring/alerting.py": '''"""Alerting system for pipeline monitoring"""
class AlertManager:
    def send_alert(self, severity: str, message: str):
        """Send alert based on severity"""
        print(f"[{severity}] {message}")
''',
        "utils/connectors/database_connector.py": '''"""Database connection utilities"""
class DatabaseConnector:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def connect(self):
        """Establish database connection"""
        pass
''',
        "utils/connectors/api_client.py": '''"""API client for external data sources"""
import requests

class APIClient:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def fetch_data(self, endpoint):
        """Fetch data from API endpoint"""
        return requests.get(f"{self.base_url}/{endpoint}")
''',
    }

    for filepath, content in utils_scripts.items():
        with open(filepath, "w") as f:
            f.write(content)

    print(f"✅ Generated {len(utils_scripts)} utility scripts")

def generate_migration_scripts():
    """Generate database migration scripts"""

    for i in range(20):
        migration_content = f'''-- Migration {i:03d}
-- Generated for Azure DevOps Sparse Checkout Demo

-- Add new columns or modify existing schema
ALTER TABLE staging.stg_stock_prices
ADD COLUMN IF NOT EXISTS migration_field_{i} VARCHAR(50);

-- Create indexes
CREATE INDEX IF NOT EXISTS idx_migration_{i}
ON staging.stg_stock_prices(migration_field_{i});

-- Update comments
COMMENT ON COLUMN staging.stg_stock_prices.migration_field_{i}
IS 'Migration field {i} added on {{{{ current_timestamp }}}}';
'''
        with open(f"data_model/migrations/migration_{i:03d}.sql", "w") as f:
            f.write(migration_content)

    print(f"✅ Generated 20 migration scripts")

def generate_documentation():
    """Generate comprehensive documentation"""

    docs = {
        "docs/architecture/system_overview.md": '''# System Architecture Overview

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
''',
        "docs/architecture/data_model.md": '''# Data Model Documentation

## Staging Layer
Contains raw ingested data with minimal transformation.

## Marts Layer
Business-focused data models optimized for analytics.

## Dimensions Layer
Reference data and slowly changing dimensions.
''',
        "docs/runbooks/incident_response.md": '''# Incident Response Runbook

## Pipeline Failures
1. Check Airflow logs
2. Verify source system availability
3. Check data quality issues
4. Restart failed tasks

## Data Quality Issues
1. Review data quality metrics
2. Check source data
3. Validate transformation logic
''',
        "docs/runbooks/deployment_guide.md": '''# Deployment Guide

## Prerequisites
- Azure DevOps account
- Database credentials
- Airflow setup

## Deployment Steps
1. Configure sparse checkout
2. Deploy selected files
3. Run migrations
4. Validate deployment
''',
    }

    for filepath, content in docs.items():
        with open(filepath, "w") as f:
            f.write(content)

    print(f"✅ Generated {len(docs)} documentation files")

def generate_sample_data():
    """Generate sample data files"""

    # CSV sample data
    csv_files = {
        "sample_data/stock_prices_sample.csv": '''symbol,price,volume,timestamp
AAPL,150.25,1000000,2024-01-01 09:30:00
GOOGL,2800.50,500000,2024-01-01 09:30:00
MSFT,380.75,750000,2024-01-01 09:30:00
''',
        "sample_data/trades_sample.csv": '''trade_id,symbol,quantity,price,timestamp
T001,AAPL,100,150.25,2024-01-01 09:35:00
T002,GOOGL,50,2800.50,2024-01-01 09:40:00
''',
    }

    for filepath, content in csv_files.items():
        with open(filepath, "w") as f:
            f.write(content)

    # JSON sample data
    json_files = {
        "sample_data/market_data_sample.json": {
            "timestamp": "2024-01-01T09:30:00Z",
            "market": "NYSE",
            "symbols": ["AAPL", "GOOGL", "MSFT"],
            "status": "open"
        },
        "sample_data/risk_metrics_sample.json": {
            "portfolio_id": "P001",
            "var_95": 1000000,
            "var_99": 1500000,
            "expected_shortfall": 1800000
        }
    }

    for filepath, data in json_files.items():
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)

    print(f"✅ Generated {len(csv_files) + len(json_files)} sample data files")

def generate_config_files():
    """Generate environment-specific config files"""

    for env in ['prod', 'staging', 'dev']:
        config_content = f'''# {env.upper()} Environment Configuration

database:
  host: {env}-db.company.com
  port: 5432
  database: financial_dw_{env}
  connection_pool_size: 20

airflow:
  dag_dir: /opt/airflow/dags
  parallelism: 16
  max_active_runs: 3

monitoring:
  enabled: true
  metrics_interval: 60
  alert_threshold: 0.95
'''
        with open(f"config/{env}/application.yaml", "w") as f:
            f.write(config_content)

    print("✅ Generated configuration files for 3 environments")

def generate_scripts():
    """Generate deployment and utility scripts"""

    scripts = {
        "scripts/deploy.sh": '''#!/bin/bash
# Deployment script for sparse checkout demo

echo "Starting deployment..."
git sparse-checkout set $(cat deployment/deploy-list.txt)
echo "Deployment complete!"
''',
        "scripts/backup.sh": '''#!/bin/bash
# Backup script

BACKUP_DIR="/backup/$(date +%Y%m%d)"
mkdir -p $BACKUP_DIR
echo "Backup created at $BACKUP_DIR"
''',
        "scripts/health_check.py": '''#!/usr/bin/env python3
"""Health check script"""
import sys

def check_database():
    return True

def check_airflow():
    return True

if __name__ == "__main__":
    if check_database() and check_airflow():
        print("✅ All systems healthy")
        sys.exit(0)
    else:
        print("❌ Health check failed")
        sys.exit(1)
''',
    }

    for filepath, content in scripts.items():
        with open(filepath, "w") as f:
            f.write(content)
        # Make scripts executable
        Path(filepath).chmod(0o755)

    print(f"✅ Generated {len(scripts)} utility scripts")

def create_additional_bulk_files():
    """Create additional files to simulate a large repository"""

    # Create test directories
    test_dirs = ["tests/unit", "tests/integration", "tests/e2e", "logs", "temp"]
    for directory in test_dirs:
        Path(directory).mkdir(parents=True, exist_ok=True)

    # Generate unit test files (30 files)
    for i in range(30):
        test_content = f'''# Test file {i}
# Generated to simulate repository size

import pytest
from utils.financial_utils import FinancialDataProcessor

def test_function_{i}():
    """Test function {i} for demo purposes"""
    processor = FinancialDataProcessor()
    assert processor is not None

class TestClass{i}:
    """Test class {i} for demo purposes"""

    def test_method_{i}(self):
        assert 1 + 1 == 2

    def test_validation_{i}(self):
        """Test data validation"""
        assert True
'''
        with open(f"tests/unit/test_module_{i}.py", "w") as f:
            f.write(test_content)

    # Generate integration test files (10 files)
    for i in range(10):
        test_content = f'''# Integration test {i}

import pytest

def test_integration_{i}():
    """Integration test for pipeline component {i}"""
    assert True
'''
        with open(f"tests/integration/test_integration_{i}.py", "w") as f:
            f.write(test_content)

    # Create log files (10 files)
    for i in range(10):
        Path(f"logs/application_{i}.log").touch()

    print("✅ Generated 50+ additional test and log files")

def main():
    """Main function to generate the demo project"""
    print("🚀 Generating Azure DevOps Sparse Checkout Demo Project...")
    print("=" * 80)

    create_directory_structure()
    generate_dag_files()
    generate_metadata_files()
    generate_data_model_files()
    generate_dbt_files()
    generate_deployment_files()
    generate_utility_files()
    generate_utility_scripts()
    generate_migration_scripts()
    generate_documentation()
    generate_sample_data()
    generate_config_files()
    generate_scripts()
    create_additional_bulk_files()

    print("=" * 80)
    print("✅ Demo project generated successfully!")
    print("\nProject Statistics:")

    # Count files by category
    def count_files_in_dir(directory):
        try:
            return len([f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))])
        except:
            return 0

    stats = {
        "DAGs": count_files_in_dir("dags"),
        "Metadata Schemas": count_files_in_dir("metadata/schemas"),
        "Config Files": count_files_in_dir("metadata/configs"),
        "Staging DDLs": count_files_in_dir("data_model/staging"),
        "Marts DDLs": count_files_in_dir("data_model/marts"),
        "Dimension DDLs": count_files_in_dir("data_model/dimensions"),
        "Migration Scripts": count_files_in_dir("data_model/migrations"),
        "DBT Staging Models": count_files_in_dir("dbt/models/staging"),
        "DBT Marts Models": count_files_in_dir("dbt/models/marts"),
        "DBT Dimension Models": count_files_in_dir("dbt/models/dimensions"),
        "DBT Macros": count_files_in_dir("dbt/macros"),
        "DBT Tests": count_files_in_dir("dbt/tests/singular"),
        "Utility Scripts": count_files_in_dir("utils") + count_files_in_dir("utils/data_quality") + count_files_in_dir("utils/monitoring"),
        "Test Files": count_files_in_dir("tests/unit") + count_files_in_dir("tests/integration"),
        "Documentation": count_files_in_dir("docs/architecture") + count_files_in_dir("docs/runbooks"),
    }

    total_files = sum(len(files) for _, _, files in os.walk(".") if not any(skip in _ for skip in ['.git', '__pycache__', '.pytest_cache']))
    total_dirs = sum(len(dirs) for _, dirs, _ in os.walk("."))

    print(f"\n📊 Detailed Breakdown:")
    for category, count in stats.items():
        print(f"   {category:.<30} {count:>4} files")

    print(f"\n📁 Total directories: {total_dirs}")
    print(f"📄 Total files: {total_files}")

    try:
        deploy_count = len([line for line in open('deployment/deploy-list.txt').readlines() if line.strip() and not line.startswith('#')])
        print(f"🎯 Deploy list contains: {deploy_count} files")
        print(f"💾 Sparse checkout saves: ~{total_files - deploy_count} files ({((total_files - deploy_count) / total_files * 100):.1f}% reduction)")
    except:
        pass

    print("\n" + "=" * 80)
    print("📋 Next Steps:")
    print("1. Initialize Git repository: git init")
    print("2. Add files: git add .")
    print("3. Commit: git commit -m 'Initial financial data pipeline project'")
    print("4. Set up Azure DevOps repository and push")
    print("5. Configure Azure DevOps pipeline for sparse checkout demo")
    print("\n💡 This large-scale project demonstrates the value of sparse checkout")
    print("   for efficient CI/CD in enterprise data engineering environments.")
    print("=" * 80)

if __name__ == "__main__":
    main()
