![ANApy](static/logo.png)
---
anapy is the beginning of a simplified universal data manipulation library for handling all forms of data

![PyPI](https://img.shields.io/pypi/v/anapy?style=for-the-badge)
![GitHub](https://img.shields.io/github/license/dirkscgm/anapy?style=for-the-badge)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/anapy?style=for-the-badge)
![GitHub top language](https://img.shields.io/github/languages/top/dirkscgm/anapy?style=for-the-badge)

## What is Anapy?

Anapy is a compact data serialization and manipulation tool. It is still WIP though the intention is to have a 
lightweight tool that can read and write to multiple data formats, as well as perform base data manipulation
tasks for Data specialists who need a quick solution for a simple problem. 

### Reading Data
ANApy has a basic reader that currently supports csv, json, yaml and sql-inserts.
```python
from anapy import data_reader as dr

data = dr.DataReader(data='data.csv', d_type='csv').read(delim=',')
data = dr.DataReader(data='data.json', d_type='json')
data = dr.DataReader(data='data.yaml', d_type='yaml')
data = dr.DataReader(data='data.sql', d_type='sql').read(sql_create=False)
```

### Writing Data
Once data has been consumed, it can be written in various formats:
```python
import anapy.data_writer as dw

dw.write_csv(file='data.csv', data=data, quoting='minimal', header=True)
dw.write_yaml(file='data.yaml', data=data)
dw.write_json(file='data.json', data=data, allow_nan=True, sort_keys=False)
```