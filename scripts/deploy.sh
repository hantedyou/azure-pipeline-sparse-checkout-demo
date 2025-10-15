#!/bin/bash
# Deployment script for sparse checkout demo

echo "Starting deployment..."
git sparse-checkout set $(cat deployment/deploy-list.txt)
echo "Deployment complete!"
