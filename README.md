# Financial Data Pipeline Demo

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
