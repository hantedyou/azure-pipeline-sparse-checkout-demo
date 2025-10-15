-- Migration 018
-- Generated for Azure DevOps Sparse Checkout Demo

-- Add new columns or modify existing schema
ALTER TABLE staging.stg_stock_prices
ADD COLUMN IF NOT EXISTS migration_field_18 VARCHAR(50);

-- Create indexes
CREATE INDEX IF NOT EXISTS idx_migration_18
ON staging.stg_stock_prices(migration_field_18);

-- Update comments
COMMENT ON COLUMN staging.stg_stock_prices.migration_field_18
IS 'Migration field 18 added on {{ current_timestamp }}';
