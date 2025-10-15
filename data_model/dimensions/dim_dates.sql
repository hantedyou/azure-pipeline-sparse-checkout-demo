-- dim_dates DDL
-- Generated for Azure DevOps Sparse Checkout Demo

CREATE TABLE IF NOT EXISTS dimensions.dim_dates (
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
CREATE INDEX idx_dim_dates_symbol ON dimensions.dim_dates(symbol);
CREATE INDEX idx_dim_dates_timestamp ON dimensions.dim_dates(timestamp);

-- Partitioning
ALTER TABLE dimensions.dim_dates 
PARTITION BY RANGE (DATE(timestamp));

-- Comments
COMMENT ON TABLE dimensions.dim_dates IS 'Dimension table for dates';
