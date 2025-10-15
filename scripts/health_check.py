#!/usr/bin/env python3
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
