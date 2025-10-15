-- fact_risk_metrics DDL
-- Generated for Azure DevOps Sparse Checkout Demo

CREATE TABLE IF NOT EXISTS marts.fact_risk_metrics (
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
CREATE INDEX idx_fact_risk_metrics_symbol ON marts.fact_risk_metrics(symbol);
CREATE INDEX idx_fact_risk_metrics_timestamp ON marts.fact_risk_metrics(timestamp);

-- Partitioning
ALTER TABLE marts.fact_risk_metrics 
PARTITION BY RANGE (DATE(timestamp));

-- Comments
COMMENT ON TABLE marts.fact_risk_metrics IS 'Data mart table for fact risk metrics';
