-- stg_stock_prices DDL
-- Generated for Azure DevOps Sparse Checkout Demo

CREATE TABLE IF NOT EXISTS staging.stg_stock_prices (
    id BIGINT IDENTITY(1,1) PRIMARY KEY,
    symbol VARCHAR(10) NOT NULL,
    price DECIMAL(18,6),
    volume BIGINT,
    timestamp TIMESTAMP NOT NULL,
    source_system VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Indexes
CREATE INDEX idx_stg_stock_prices_symbol ON staging.stg_stock_prices(symbol);
CREATE INDEX idx_stg_stock_prices_timestamp ON staging.stg_stock_prices(timestamp);

-- Partitioning
ALTER TABLE staging.stg_stock_prices 
PARTITION BY RANGE (DATE(timestamp));

-- Comments
COMMENT ON TABLE staging.stg_stock_prices IS 'Staging table for stock prices';
