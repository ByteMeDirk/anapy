import ast
import base64
import gzip
import os
import shutil


def list_tables():
    """list current tables in stash"""
    return os.listdir('stash/')


def delete_tables(table):
    """
    delete the table within the stash directory
    :param table: table to delete
    """
    try:
        shutil.rmtree(f'stash/{table}')
    except FileNotFoundError:
        raise FileNotFoundError(f'{table} is not a stashed table, '
                                'stashed tables are: \n'
                                f'{list_tables()}')


class StashTable:
    """
    StashTable is a simplistic data storage solution for
    quickly reading and writing datasets in a compressed
    columnar storage system. The solution runs locally
    within your application.
    The benefit of the columnar storage method is rapid
    search capabilities on relatively large data
    being piped in and out of the application.


    # get data
    data = dr.DataReader(data='data.csv').read()

    # stash data to table
    table = StashTable(data=data, table='basic_csv')

    col_names = table.col_names()
    print(col_names)

    first_row = table.row(index=0)
    print(first_row)

    first_col = table.col(key='email')
    print(first_col)

    subset = table.get(key='subs', value='15', operator='==')

    table.delete()

    """

    def __init__(self, **kwargs):
        self.data = kwargs['data']
        self.table = kwargs['table']
        self.keys = list(k for k in self.data[0].keys())

        self.cwd = os.getcwd() + '/stash/'

        try:
            os.makedirs(f'stash/{self.table}')
        except FileExistsError:
            pass

    def __bin_read(self, key):
        """ reads from binary ANApy file structure """
        try:
            with gzip.open(f'{self.cwd}/{self.table}/{key}', 'r') as f:
                dat = ast.literal_eval(base64.decodebytes(f.read()).decode())
                return dat
        except FileNotFoundError:
            raise ValueError(f'the column: "{key}" '
                             f'does not exist or has not been stashed')

    def __bin_write(self, key, values):
        """ writes to binary in ANApy file structure """
        with gzip.open(f'{self.cwd}/{self.table}/{key}', 'wb') as f:
            dat = base64.encodebytes(str(values).encode())
            f.write(dat)

    def save(self):
        """  stash data table to ANApy columnar file structure """
        values = []
        for k in self.keys:
            for i in range(len(self.data)):
                values.append(f'{self.data[i][k]}')

            self.__bin_write(k, values)
            values = []

    def col(self, key) -> list:
        """
        return column from stashed data table
        :param key: str: name of column
        :return: list: column values
        """
        return self.__bin_read(key=key)

    def row(self, index) -> dict:
        """
        return row from stashed data table
        :param index: int: index of the row in
        :return: dict: key value pair of row
        """
        __row = {}

        for key in self.keys:
            tmp = self.__bin_read(key=key)
            __row[key] = tmp[index]

        return __row

    def col_names(self):
        """ returns column naves or keys of table """
        return self.keys

    def get(self, key, value, operator) -> list:
        # ToDo: not very efficient, work on something a little faster
        """
        return all rows where a key.value matches a specific value
        note that the logical operator is not sensitive to data type and will
        return anything that is true
        :param key: str: column name
        :param value: str: value where key.value matches based on operator
        :param operator: str: logical operator [>, <, >=, <=, !=, ==]
        :return: list: list of dictionary containing matching data
        """
        ops = {
            '>': lambda a, b: a > b,
            '<': lambda a, b: a < b,
            '>=': lambda a, b: a >= b,
            '<=': lambda a, b: a <= b,
            '!=': lambda a, b: a != b,
            '==': lambda a, b: a == b
        }

        search_list, tmp = [], []
        col_data = self.col(key=key)

        try:
            func = ops[operator]
        except KeyError:
            raise ValueError(f'{operator} is not a valid operator')

        # get data index where value equals
        for i in range(len(col_data)):
            if func(col_data[i], value):
                search_list.append(i)

        # return rows of equal data
        for i in search_list:
            tmp.append(self.row(index=i))

        return tmp

    def delete(self):
        """ delete the table once all work has been completed """
        shutil.rmtree(f'stash/{self.table}')

    @staticmethod
    def un_stash():
        """ delete the ANApy stash system """
        os.rmdir('stash')
        shutil.rmtree('stash')
