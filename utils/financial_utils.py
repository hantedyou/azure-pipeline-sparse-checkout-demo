#!/usr/bin/env python3
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
