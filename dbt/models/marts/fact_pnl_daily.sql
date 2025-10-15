{{
  config(
    materialized='table',
    schema='marts',
    indexes=[
      {'columns': ['symbol'], 'type': 'btree'},
      {'columns': ['date'], 'type': 'btree'}
    ]
  )
}}

-- fact_pnl_daily mart model
-- Generated for Azure DevOps Sparse Checkout Demo

SELECT
    symbol,
    date,
    AVG(price) AS avg_price,
    MIN(price) AS min_price,
    MAX(price) AS max_price,
    SUM(volume) AS total_volume,
    COUNT(*) AS trade_count,
    CURRENT_TIMESTAMP AS created_at
FROM {{ ref('stg_stock_prices') }}
WHERE date >= CURRENT_DATE - INTERVAL '30 days'
GROUP BY symbol, date
