-- Migration 001
-- Generated for Azure DevOps Sparse Checkout Demo

-- Add new columns or modify existing schema
ALTER TABLE staging.stg_stock_prices
ADD COLUMN IF NOT EXISTS migration_field_1 VARCHAR(50);

-- Create indexes
CREATE INDEX IF NOT EXISTS idx_migration_1
ON staging.stg_stock_prices(migration_field_1);

-- Update comments
COMMENT ON COLUMN staging.stg_stock_prices.migration_field_1
IS 'Migration field 1 added on {{ current_timestamp }}';
