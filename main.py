import anapy.data_reader as dr
import anapy.data_writer as dw
import anapy.stash as st
from anapy.analyse import Analyse
from anapy.stash import StashTable


def standard_stash():
    """example of a normal data read, stash and write"""

    data = dr.DataReader(data='test/data/json_array.json.gz', format='json.gz').read()
    dw.write_csv(data=data, file='main.csv')

    table = StashTable(data=data, table='basic')
    table.save()

    col_names = table.col_names()
    first_row = table.row(index=0)
    first_col = table.col(key='id')

    subset = table.get(key='gender', value='Female', operator='==', reindex=True)
    dw.write_csv(data=subset, file='subset.csv')

    table.un_stash()


def analyse_stash():
    """example of using analysis on stashed table"""

    data = dr.DataReader(data='test/data/json_array.json.gz', format='json.gz').read()
    table = StashTable(data=data, table='basic')
    table.save()

    table_ana = Analyse(table='basic')  # stashed table name needs to be specified

    print(table_ana.max(col='id'))
    print(table_ana.min(col='id'))
    print(table_ana.mean(col='id'))
    print(table_ana.mode(col='id'))
    print(table_ana.median(col='id'))

    table.un_stash()


if __name__ == '__main__':
    analyse_stash()
