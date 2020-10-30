from anapy import data_reader as dr
import anapy.data_writer as dw

sql_dat = dr.DataReader(data='tests/data/sql_create.sql').read(sql_create=True)
csv_dat = dr.DataReader(data='tests/data/basic_csv.csv').read()

dw.write_yaml(data=sql_dat, file='sql_to_csv.yaml')

