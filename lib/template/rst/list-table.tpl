{% macro display_list_table(rows) -%}
.. list-table:: 
   :header-rows: 1
{%- for row in rows %}
  {% for col in row %}
   {% if loop.first -%}*{% else %} {% endif %} - {{ col }} 
  {%- endfor %}
{%- endfor %}
{%- endmacro %}

