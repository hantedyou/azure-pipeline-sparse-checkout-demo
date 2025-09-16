-- stg_risk_exposures DDL
-- Generated for Azure DevOps Sparse Checkout Demo

CREATE TABLE IF NOT EXISTS staging.stg_risk_exposures (
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
CREATE INDEX idx_stg_risk_exposures_symbol ON staging.stg_risk_exposures(symbol);
CREATE INDEX idx_stg_risk_exposures_timestamp ON staging.stg_risk_exposures(timestamp);

-- Partitioning
ALTER TABLE staging.stg_risk_exposures 
PARTITION BY RANGE (DATE(timestamp));

-- Comments
COMMENT ON TABLE staging.stg_risk_exposures IS 'Staging table for risk exposures';
