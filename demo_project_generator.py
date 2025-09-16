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
        "dbt/models/staging",
        "dbt/models/marts",
        "dbt/models/dimensions",
        "dbt/macros",
        "dbt/tests",
        "deployment",
        "utils",
        "docs"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
    print(f"✅ Created {len(directories)} directories")

def generate_dag_files():
    """Generate 20 DAG files for financial data pipelines"""
    dag_templates = [
        # Market Data
        "stock_price_ingestion", "bond_yield_analysis", "forex_rates_pipeline",
        "commodity_prices_etl", "crypto_market_data", "options_chain_ingestion",
        "futures_contracts_etl", "market_indices_pipeline", "earnings_data_ingestion",
        
        # Trading & Risk
        "trade_settlement_pipeline", "risk_exposure_calculation", "portfolio_valuation_etl",
        "margin_requirements_analysis", "credit_risk_assessment", "market_risk_pipeline",
        
        # Regulatory & Compliance
        "regulatory_reporting_pipeline", "compliance_monitoring_etl", "audit_trail_ingestion",
        "kyc_data_pipeline", "aml_transaction_monitoring"
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
    
    # Schema files
    schemas = [
        "stock_price_schema.json", "bond_yield_schema.json", "forex_rates_schema.json",
        "trade_settlement_schema.json", "risk_exposure_schema.json", "portfolio_schema.json"
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
    
    # Config files  
    configs = [
        "database_connections.yaml", "data_quality_rules.yaml", "monitoring_config.yaml"
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
    
    # Staging DDLs
    staging_tables = [
        "stg_stock_prices", "stg_bond_yields", "stg_forex_rates",
        "stg_trade_settlements", "stg_risk_exposures"
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
    
    # Marts DDLs
    marts_tables = ["dim_securities", "dim_counterparties", "fact_trades", "fact_positions"]
    
    for table in marts_tables:
        content = ddl_template.format(
            table_name=table,
            schema='marts',
            description=f'Data mart table for {table.replace("_", " ")}'
        )
        with open(f"data_model/marts/{table}.sql", "w") as f:
            f.write(content)
    
    print(f"✅ Generated {len(staging_tables + marts_tables)} DDL files")

def generate_dbt_files():
    """Generate DBT models and SQL files"""
    
    # Staging models
    staging_models = [
        "stg_stock_prices", "stg_bond_yields", "stg_forex_rates",
        "stg_trade_settlements", "stg_risk_exposures"
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
    
    # Mart models
    marts_models = ["dim_securities", "fact_daily_prices", "fact_trade_summary"]
    
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
    
    # DBT macros
    macro_content = '''-- Common macros for financial data processing
-- Generated for Azure DevOps Sparse Checkout Demo

{% macro calculate_returns(price_column, periods=1) %}
  ({{ price_column }} - LAG({{ price_column }}, {{ periods }}) OVER (ORDER BY timestamp)) 
  / LAG({{ price_column }}, {{ periods }}) OVER (ORDER BY timestamp) * 100
{% endmacro %}

{% macro clean_symbol(symbol_column) %}
  UPPER(TRIM({{ symbol_column }}))
{% endmacro %}
'''
    
    with open("dbt/macros/financial_calculations.sql", "w") as f:
        f.write(macro_content)
    
    print(f"✅ Generated {len(staging_models + marts_models)} DBT models and macros")

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

def create_additional_bulk_files():
    """Create additional files to simulate a large repository"""
    
    # Create some test files
    test_dirs = ["tests/unit", "tests/integration", "logs", "temp"]
    for directory in test_dirs:
        Path(directory).mkdir(parents=True, exist_ok=True)
    
    # Generate some dummy test files
    for i in range(10):
        test_content = f'''# Test file {i}
# Generated to simulate repository size

def test_function_{i}():
    """Dummy test function for demo purposes"""
    assert True

class TestClass{i}:
    """Dummy test class for demo purposes"""
    
    def test_method(self):
        assert 1 + 1 == 2
'''
        with open(f"tests/unit/test_module_{i}.py", "w") as f:
            f.write(test_content)
    
    # Create some log files (empty)
    for i in range(5):
        Path(f"logs/application_{i}.log").touch()
    
    print("✅ Generated additional bulk files")

def main():
    """Main function to generate the demo project"""
    print("🚀 Generating Azure DevOps Sparse Checkout Demo Project...")
    print("=" * 60)
    
    create_directory_structure()
    generate_dag_files()
    generate_metadata_files()
    generate_data_model_files()
    generate_dbt_files()
    generate_deployment_files()
    generate_utility_files()
    create_additional_bulk_files()
    
    print("=" * 60)
    print("✅ Demo project generated successfully!")
    print("\nProject Statistics:")
    
    # Count files
    total_files = sum(len(files) for _, _, files in os.walk("."))
    total_dirs = sum(len(dirs) for _, dirs, _ in os.walk("."))
    
    print(f"📁 Total directories: {total_dirs}")
    print(f"📄 Total files: {total_files}")
    print(f"🎯 Deploy list contains: {len(open('deployment/deploy-list.txt').readlines()) - 2} files")
    print("\nNext steps:")
    print("1. Initialize Git repository: git init")
    print("2. Add files: git add .")
    print("3. Commit: git commit -m 'Initial financial data pipeline project'")
    print("4. Set up Azure DevOps repository and push")
    print("5. Configure Azure DevOps pipeline for sparse checkout demo")

if __name__ == "__main__":
    main()
