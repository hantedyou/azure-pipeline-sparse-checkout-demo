{{
  config(
    materialized='table',
    schema='dimensions'
  )
}}

-- dim_traders dimension model
SELECT DISTINCT
    id,
    name,
    type,
    created_at,
    updated_at
FROM {{ ref('stg_security_master') }}
