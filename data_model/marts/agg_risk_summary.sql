-- agg_risk_summary DDL
-- Generated for Azure DevOps Sparse Checkout Demo

CREATE TABLE IF NOT EXISTS marts.agg_risk_summary (
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
CREATE INDEX idx_agg_risk_summary_symbol ON marts.agg_risk_summary(symbol);
CREATE INDEX idx_agg_risk_summary_timestamp ON marts.agg_risk_summary(timestamp);

-- Partitioning
ALTER TABLE marts.agg_risk_summary 
PARTITION BY RANGE (DATE(timestamp));

-- Comments
COMMENT ON TABLE marts.agg_risk_summary IS 'Data mart table for agg risk summary';
