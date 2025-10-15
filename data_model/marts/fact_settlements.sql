-- fact_settlements DDL
-- Generated for Azure DevOps Sparse Checkout Demo

CREATE TABLE IF NOT EXISTS marts.fact_settlements (
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
CREATE INDEX idx_fact_settlements_symbol ON marts.fact_settlements(symbol);
CREATE INDEX idx_fact_settlements_timestamp ON marts.fact_settlements(timestamp);

-- Partitioning
ALTER TABLE marts.fact_settlements 
PARTITION BY RANGE (DATE(timestamp));

-- Comments
COMMENT ON TABLE marts.fact_settlements IS 'Data mart table for fact settlements';
