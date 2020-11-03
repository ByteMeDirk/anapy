import anapy.data_reader as dr
import anapy.data_writer as dw
from anapy.stash import StashTable


def main():
    data = dr.DataReader(data='test/data/json_array.json.gz', format='json.gz').read()

    table = StashTable(data=data, table='basic')
    table.save()

    col_names = table.col_names()
    first_row = table.row(index=0)
    first_col = table.col(key='email')

    females = table.get(key='gender', value='Female', operator='==')
    dw.write_csv(data=females, file='female_subset.csv')

    table.un_stash()


if __name__ == '__main__':
    main()
