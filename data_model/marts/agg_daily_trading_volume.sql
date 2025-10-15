-- agg_daily_trading_volume DDL
-- Generated for Azure DevOps Sparse Checkout Demo

CREATE TABLE IF NOT EXISTS marts.agg_daily_trading_volume (
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
CREATE INDEX idx_agg_daily_trading_volume_symbol ON marts.agg_daily_trading_volume(symbol);
CREATE INDEX idx_agg_daily_trading_volume_timestamp ON marts.agg_daily_trading_volume(timestamp);

-- Partitioning
ALTER TABLE marts.agg_daily_trading_volume 
PARTITION BY RANGE (DATE(timestamp));

-- Comments
COMMENT ON TABLE marts.agg_daily_trading_volume IS 'Data mart table for agg daily trading volume';
