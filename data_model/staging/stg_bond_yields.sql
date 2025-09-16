-- stg_bond_yields DDL
-- Generated for Azure DevOps Sparse Checkout Demo

CREATE TABLE IF NOT EXISTS staging.stg_bond_yields (
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
CREATE INDEX idx_stg_bond_yields_symbol ON staging.stg_bond_yields(symbol);
CREATE INDEX idx_stg_bond_yields_timestamp ON staging.stg_bond_yields(timestamp);

-- Partitioning
ALTER TABLE staging.stg_bond_yields 
PARTITION BY RANGE (DATE(timestamp));

-- Comments
COMMENT ON TABLE staging.stg_bond_yields IS 'Staging table for bond yields';
