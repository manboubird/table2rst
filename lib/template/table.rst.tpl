{% extends "base.rst.tpl" %}
{% import 'rst/list-table.tpl' as rst %}

{% block tables scoped %}
  {%- for rows in tables %}
{{ rst.display_list_table(rows) }}
  {% endfor %}
{% endblock %}

