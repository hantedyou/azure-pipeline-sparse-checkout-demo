"""Alerting system for pipeline monitoring"""
class AlertManager:
    def send_alert(self, severity: str, message: str):
        """Send alert based on severity"""
        print(f"[{severity}] {message}")
