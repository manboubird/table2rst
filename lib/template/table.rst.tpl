{% extends "base.rst.tpl" %}

{% block tables scoped %}
  {%- for rows in tables %}
{{ display_rst_list_table(rows) }}
  {% endfor %}
{% endblock %}

