-- stg_margin_calls DDL
-- Generated for Azure DevOps Sparse Checkout Demo

CREATE TABLE IF NOT EXISTS staging.stg_margin_calls (
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
CREATE INDEX idx_stg_margin_calls_symbol ON staging.stg_margin_calls(symbol);
CREATE INDEX idx_stg_margin_calls_timestamp ON staging.stg_margin_calls(timestamp);

-- Partitioning
ALTER TABLE staging.stg_margin_calls 
PARTITION BY RANGE (DATE(timestamp));

-- Comments
COMMENT ON TABLE staging.stg_margin_calls IS 'Staging table for margin calls';
