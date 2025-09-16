-- dim_counterparties DDL
-- Generated for Azure DevOps Sparse Checkout Demo

CREATE TABLE IF NOT EXISTS marts.dim_counterparties (
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
CREATE INDEX idx_dim_counterparties_symbol ON marts.dim_counterparties(symbol);
CREATE INDEX idx_dim_counterparties_timestamp ON marts.dim_counterparties(timestamp);

-- Partitioning
ALTER TABLE marts.dim_counterparties 
PARTITION BY RANGE (DATE(timestamp));

-- Comments
COMMENT ON TABLE marts.dim_counterparties IS 'Data mart table for dim counterparties';
