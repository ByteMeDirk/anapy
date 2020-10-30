from anapy import data_reader as dr
from anapy import data_writer as dw

tmp1 = dr.DataReader(data='tests/data/MOCK_DATA.csv')
tmp1 = tmp1.read()

tmp2 = dr.DataReader(data='tests/data/MOCK_DATA.json')
tmp2 = tmp2.read()

tmp3 = dr.DataReader(data='tests/data/MOCK_DATA', d_type='csv')
tmp3 = tmp3.read()

tmp4 = dr.DataReader(data='tests/data/MOCK_DATA.yaml')
tmp4 = tmp4.read()


print(tmp1)



dw.DataWriter(data=tmp1, file='tmp.csv').write(format='csv', header=False, quoting='minimal')

