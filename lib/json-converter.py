#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import pandas as pd
from pandas.io.json import json_normalize
from jinja2 import Environment, FileSystemLoader


def get_rows(df, display_columns=[], drop_columns=[]):
  df = df.reindex_axis(display_columns, axis=1)
  df = df.drop(drop_columns, axis=1)
  rows = [df.columns.tolist()] + df.values.tolist()
  return rows


file = "data/boto-ec2-describe_addresses.json"

with open(file) as data_file:    
  data = json.load(data_file)

root_key_name = 'Addresses'
display_columns = ['InstanceId', 'PublicIp', 'Domain', 'AllocationId', 'AssociationId', 'NetworkInterfaceId', 'NetworkInterfaceOwnerId', 'PrivateIpAddress']

df = json_normalize(data, root_key_name)
rows = get_rows(df, display_columns=display_columns)

tpl_env = Environment(loader=FileSystemLoader('./lib/template', encoding='utf8'))
tpl = tpl_env.get_template('table.rst.tpl')
rst = tpl.render({'title': file, 'tables': [ rows ]})
print rst.encode('utf-8')
