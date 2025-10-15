-- Migration 003
-- Generated for Azure DevOps Sparse Checkout Demo

-- Add new columns or modify existing schema
ALTER TABLE staging.stg_stock_prices
ADD COLUMN IF NOT EXISTS migration_field_3 VARCHAR(50);

-- Create indexes
CREATE INDEX IF NOT EXISTS idx_migration_3
ON staging.stg_stock_prices(migration_field_3);

-- Update comments
COMMENT ON COLUMN staging.stg_stock_prices.migration_field_3
IS 'Migration field 3 added on {{ current_timestamp }}';
