"""
Security Master Sync DAG for financial data processing
Generated for Azure DevOps Sparse Checkout Demo
"""

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'data_engineering_team',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'security_master_sync',
    default_args=default_args,
    description='Process security master sync for financial analysis',
    schedule_interval='@daily',
    catchup=False,
    tags=['market_data', 'trading']
)

def extract_data():
    """Extract data from source systems"""
    print("Extracting security data...")
    # Demo: Simulate data extraction
    pass

def transform_data():
    """Transform and validate data"""
    print("Transforming security data...")
    # Demo: Simulate data transformation
    pass

def load_data():
    """Load data to target warehouse"""
    print("Loading security data to warehouse...")
    # Demo: Simulate data loading
    pass

# Define tasks
extract_task = PythonOperator(
    task_id='extract_security',
    python_callable=extract_data,
    dag=dag
)

transform_task = PythonOperator(
    task_id='transform_security',
    python_callable=transform_data,
    dag=dag
)

load_task = PythonOperator(
    task_id='load_security',
    python_callable=load_data,
    dag=dag
)

# Task dependencies
extract_task >> transform_task >> load_task
