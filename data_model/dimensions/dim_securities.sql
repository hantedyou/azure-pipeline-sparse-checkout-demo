-- dim_securities DDL
-- Generated for Azure DevOps Sparse Checkout Demo

CREATE TABLE IF NOT EXISTS dimensions.dim_securities (
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
CREATE INDEX idx_dim_securities_symbol ON dimensions.dim_securities(symbol);
CREATE INDEX idx_dim_securities_timestamp ON dimensions.dim_securities(timestamp);

-- Partitioning
ALTER TABLE dimensions.dim_securities 
PARTITION BY RANGE (DATE(timestamp));

-- Comments
COMMENT ON TABLE dimensions.dim_securities IS 'Dimension table for securities';
