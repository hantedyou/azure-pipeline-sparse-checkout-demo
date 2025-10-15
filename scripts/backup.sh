#!/bin/bash
# Backup script

BACKUP_DIR="/backup/$(date +%Y%m%d)"
mkdir -p $BACKUP_DIR
echo "Backup created at $BACKUP_DIR"
