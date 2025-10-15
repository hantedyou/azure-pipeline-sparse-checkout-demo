-- Migration 002
-- Generated for Azure DevOps Sparse Checkout Demo

-- Add new columns or modify existing schema
ALTER TABLE staging.stg_stock_prices
ADD COLUMN IF NOT EXISTS migration_field_2 VARCHAR(50);

-- Create indexes
CREATE INDEX IF NOT EXISTS idx_migration_2
ON staging.stg_stock_prices(migration_field_2);

-- Update comments
COMMENT ON COLUMN staging.stg_stock_prices.migration_field_2
IS 'Migration field 2 added on {{ current_timestamp }}';
