-- Date utility macros
{% macro get_business_days(start_date, end_date) %}
  SELECT COUNT(*) FROM dim_dates
  WHERE date BETWEEN {{ start_date }} AND {{ end_date }}
  AND is_business_day = TRUE
{% endmacro %}
