-- stg_options_chain DDL
-- Generated for Azure DevOps Sparse Checkout Demo

CREATE TABLE IF NOT EXISTS staging.stg_options_chain (
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
CREATE INDEX idx_stg_options_chain_symbol ON staging.stg_options_chain(symbol);
CREATE INDEX idx_stg_options_chain_timestamp ON staging.stg_options_chain(timestamp);

-- Partitioning
ALTER TABLE staging.stg_options_chain 
PARTITION BY RANGE (DATE(timestamp));

-- Comments
COMMENT ON TABLE staging.stg_options_chain IS 'Staging table for options chain';
