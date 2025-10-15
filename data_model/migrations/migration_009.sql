-- Migration 009
-- Generated for Azure DevOps Sparse Checkout Demo

-- Add new columns or modify existing schema
ALTER TABLE staging.stg_stock_prices
ADD COLUMN IF NOT EXISTS migration_field_9 VARCHAR(50);

-- Create indexes
CREATE INDEX IF NOT EXISTS idx_migration_9
ON staging.stg_stock_prices(migration_field_9);

-- Update comments
COMMENT ON COLUMN staging.stg_stock_prices.migration_field_9
IS 'Migration field 9 added on {{ current_timestamp }}';
