"""Metrics collection for monitoring"""
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
