"""
Aml Transaction Monitoring DAG for financial data processing
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
    'aml_transaction_monitoring',
    default_args=default_args,
    description='Process aml transaction monitoring for financial analysis',
    schedule_interval='@daily',
    catchup=False,
    tags=['market_data', 'real_time']
)

def extract_data():
    """Extract data from source systems"""
    print("Extracting aml data...")
    # Demo: Simulate data extraction
    pass

def transform_data():
    """Transform and validate data"""
    print("Transforming aml data...")
    # Demo: Simulate data transformation
    pass

def load_data():
    """Load data to target warehouse"""
    print("Loading aml data to warehouse...")
    # Demo: Simulate data loading
    pass

# Define tasks
extract_task = PythonOperator(
    task_id='extract_aml',
    python_callable=extract_data,
    dag=dag
)

transform_task = PythonOperator(
    task_id='transform_aml',
    python_callable=transform_data,
    dag=dag
)

load_task = PythonOperator(
    task_id='load_aml',
    python_callable=load_data,
    dag=dag
)

# Task dependencies
extract_task >> transform_task >> load_task
