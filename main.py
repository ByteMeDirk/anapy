import anapy.data_writer as dw
from anapy import data_reader as dr


def main():
    csv_dat = dr.DataReader(data='tests/data/sql_insert.sql').read()
    print(csv_dat[0])

    data = dr.DataReader(data='data.sql', d_type='sql').read(sql_create=False)

    dw.write_csv(file='data.csv', data=data, quoting='minimal', header=True)
    dw.write_yaml(file='data.yaml', data=data)
    dw.write_json(file='data.json', data=data, allow_nan=True, sort_keys=False)


if __name__ == '__main__':
    main()
