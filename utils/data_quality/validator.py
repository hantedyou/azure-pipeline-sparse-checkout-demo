"""Data quality validation utilities"""
import pandas as pd
from typing import Dict, List

class DataValidator:
    def validate_schema(self, df: pd.DataFrame, expected_schema: Dict) -> bool:
        """Validate dataframe schema"""
        return all(col in df.columns for col in expected_schema.keys())

    def check_null_percentage(self, df: pd.DataFrame, threshold: float = 0.1) -> Dict:
        """Check null percentage for each column"""
        return {col: df[col].isnull().mean() for col in df.columns}
