-- Common macros for financial data processing
-- Generated for Azure DevOps Sparse Checkout Demo

{% macro calculate_returns(price_column, periods=1) %}
  ({{ price_column }} - LAG({{ price_column }}, {{ periods }}) OVER (ORDER BY timestamp)) 
  / LAG({{ price_column }}, {{ periods }}) OVER (ORDER BY timestamp) * 100
{% endmacro %}

{% macro clean_symbol(symbol_column) %}
  UPPER(TRIM({{ symbol_column }}))
{% endmacro %}
