-- Test Price Anomalies
SELECT * FROM {{ ref('stg_stock_prices') }}
WHERE price < 0 OR price > 1000000
