-- Data quality macros
{% macro check_null_values(column_name) %}
  COUNT(CASE WHEN {{ column_name }} IS NULL THEN 1 END)
{% endmacro %}

{% macro check_duplicates(columns) %}
  COUNT(*) - COUNT(DISTINCT {{ columns }})
{% endmacro %}
