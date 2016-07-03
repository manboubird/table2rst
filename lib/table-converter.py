#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jinja2 import Environment, FileSystemLoader
import pandas as pd
import numpy as np


def get_rows(df, start_idx=0):
  idx = start_idx
  cur = df.iloc[idx]
  non_na_cnt = cur.dropna()
  rows = []
  while len(non_na_cnt) > 0:
    idx += 1
    display_row = cur.fillna('').values
    rows.append(display_row)
    cur = df.iloc[idx]
    non_na_cnt = cur.dropna()
  return rows


def display_rst_list_table(rows):
  tpl = env.get_template('rst/list-table.tpl')
  return tpl.render({'rows': rows})

def get_template_env():
  env = Environment(loader=FileSystemLoader('./lib/template', encoding='utf8'))
  env.globals['display_rst_list_table'] = display_rst_list_table
  return env

env = get_template_env()

file = "data/test.csv"
# df = pd.ExcelFile(file).parse(sheet)
df = pd.read_csv(file, header=None, encoding="utf-8") 
start_idx = 36
rows = get_rows(df, start_idx)


tpl = env.get_template('table.rst.tpl')
rst = tpl.render({'title': file, 'tables': [ rows, rows ]})
print rst.encode('utf-8')

