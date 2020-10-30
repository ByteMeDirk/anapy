from anapy import data_reader as dr
import anapy.data_writer as dw

# csv_dat = dr.DataReader(data='tests/data/sql_insert.sql').read()
# print(csv_dat[0])

csv_dat = dr.DataReader(data='tests/data/sql_insert.sql').read()
csv_dat1 = dr.DataReader(data='tests/data/sql_insert.sql.gz').read()
