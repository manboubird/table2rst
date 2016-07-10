#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pandas.io.json import json_normalize
from jinja2 import Environment, FileSystemLoader
import pandas as pd
import numpy as np
import json


def get_csv_rows(df, start_idx=0):
  idx = start_idx
  cur = df.iloc[idx]
  non_na_cnt = cur.dropna()
  rows = []
  while len(non_na_cnt) > 0:
    idx += 1
    display_row = cur.fillna('').str.replace('\n', '').values
    rows.append(display_row)
    cur = df.iloc[idx]
    non_na_cnt = cur.dropna()
  return rows

def get_json_rows(df, display_columns=[], drop_columns=[]):
  df = df.reindex_axis(display_columns, axis=1)
  df = df.drop(drop_columns, axis=1)
  rows = [df.columns.tolist()] + df.values.tolist()
  return rows


# csv
csv_file = "data/test.csv"
csv_df = pd.read_csv(csv_file, header=None, encoding="utf-8") 
start_idx = 36
csv_rows = get_csv_rows(csv_df, start_idx)


# json
json_file = "data/boto-ec2-describe_addresses.json"

with open(json_file) as data_file:    
  json_data = json.load(data_file)

root_key_name = 'Addresses'
display_columns = ['InstanceId', 'PublicIp', 'Domain', 'AllocationId', 'AssociationId', 'NetworkInterfaceId', 'NetworkInterfaceOwnerId', 'PrivateIpAddress']

json_df = json_normalize(json_data, root_key_name)
json_rows = get_json_rows(json_df, display_columns=display_columns)


def datetime_format(value, format='%Y/%m/%d %H:%M'):
  return value.strftime(format)

from datetime import datetime as dt

tpl_env = Environment(loader=FileSystemLoader('./lib/template', encoding='utf8'))
tpl_env.filters['datetime_format'] = datetime_format

tpl = tpl_env.get_template('table.rst.tpl')

rst = tpl.render({'title': file, 'tables': [ csv_rows, json_rows ], 'pub_date': dt.now()})
print rst.encode('utf-8')

