"""Anomaly detection for financial data"""
import numpy as np

class AnomalyDetector:
    def detect_outliers(self, data, method='iqr'):
        """Detect outliers using IQR or Z-score"""
        if method == 'iqr':
            Q1 = np.percentile(data, 25)
            Q3 = np.percentile(data, 75)
            IQR = Q3 - Q1
            return (data < Q1 - 1.5 * IQR) | (data > Q3 + 1.5 * IQR)
