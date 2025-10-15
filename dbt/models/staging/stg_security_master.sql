{{
  config(
    materialized='view',
    schema='staging'
  )
}}

-- stg_security_master staging model
-- Generated for Azure DevOps Sparse Checkout Demo

SELECT
    id,
    symbol,
    CAST(price AS DECIMAL(18,6)) AS price,
    volume,
    timestamp,
    source_system,
    created_at,
    updated_at
FROM {{ source('raw', 'raw_security_master') }}
WHERE timestamp >= CURRENT_DATE - INTERVAL '7 days'
  AND price IS NOT NULL
  AND symbol IS NOT NULL
