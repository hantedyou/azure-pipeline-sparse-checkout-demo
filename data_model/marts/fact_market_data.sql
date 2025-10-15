-- fact_market_data DDL
-- Generated for Azure DevOps Sparse Checkout Demo

CREATE TABLE IF NOT EXISTS marts.fact_market_data (
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
CREATE INDEX idx_fact_market_data_symbol ON marts.fact_market_data(symbol);
CREATE INDEX idx_fact_market_data_timestamp ON marts.fact_market_data(timestamp);

-- Partitioning
ALTER TABLE marts.fact_market_data 
PARTITION BY RANGE (DATE(timestamp));

-- Comments
COMMENT ON TABLE marts.fact_market_data IS 'Data mart table for fact market data';
