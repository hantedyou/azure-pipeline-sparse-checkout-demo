-- dim_traders DDL
-- Generated for Azure DevOps Sparse Checkout Demo

CREATE TABLE IF NOT EXISTS dimensions.dim_traders (
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
CREATE INDEX idx_dim_traders_symbol ON dimensions.dim_traders(symbol);
CREATE INDEX idx_dim_traders_timestamp ON dimensions.dim_traders(timestamp);

-- Partitioning
ALTER TABLE dimensions.dim_traders 
PARTITION BY RANGE (DATE(timestamp));

-- Comments
COMMENT ON TABLE dimensions.dim_traders IS 'Dimension table for traders';
