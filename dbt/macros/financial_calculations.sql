-- Financial calculation macros
{% macro calculate_returns(price_column, periods=1) %}
  ({{ price_column }} - LAG({{ price_column }}, {{ periods }}) OVER (ORDER BY timestamp))
  / LAG({{ price_column }}, {{ periods }}) OVER (ORDER BY timestamp) * 100
{% endmacro %}

{% macro calculate_sharpe_ratio(returns, risk_free_rate=0.02) %}
  (AVG({{ returns }}) - {{ risk_free_rate }}) / STDDEV({{ returns }})
{% endmacro %}
