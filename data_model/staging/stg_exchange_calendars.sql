-- stg_exchange_calendars DDL
-- Generated for Azure DevOps Sparse Checkout Demo

CREATE TABLE IF NOT EXISTS staging.stg_exchange_calendars (
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
CREATE INDEX idx_stg_exchange_calendars_symbol ON staging.stg_exchange_calendars(symbol);
CREATE INDEX idx_stg_exchange_calendars_timestamp ON staging.stg_exchange_calendars(timestamp);

-- Partitioning
ALTER TABLE staging.stg_exchange_calendars 
PARTITION BY RANGE (DATE(timestamp));

-- Comments
COMMENT ON TABLE staging.stg_exchange_calendars IS 'Staging table for exchange calendars';
