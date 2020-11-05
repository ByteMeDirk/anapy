import ast
import base64
import gzip
import os
import shutil

from anapy import utils


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
        """Reads from binary ANApy file structure"""
        try:
            file = f'{self.cwd}/{self.table}/{key}'
            return utils.binary_read(file)
        except FileNotFoundError:
            raise ValueError(f'the column: "{key}" '
                             f'does not exist or has not been stashed')

    def __bin_write(self, key, values):
        """Writes to binary in ANApy file structure"""
        file = f'{self.cwd}/{self.table}/{key}'
        utils.binary_write(file=file, data=values)

    def save(self):
        """Stash data table to ANApy columnar file structure"""
        values = []
        for k in self.keys:
            for i in range(len(self.data)):
                values.append(f'{self.data[i][k]}')

            self.__bin_write(k, values)
            values = []

    def col(self, key) -> list:
        """
        Return column from stashed data table
        :param key: str: name of column
        :return: list: column values
        """
        return self.__bin_read(key=key)

    def row(self, index) -> dict:
        """
        Return row from stashed data table
        :param index: int: index of the row in
        :return: dict: key value pair of row
        """
        __row = {}

        for key in self.keys:
            tmp = self.__bin_read(key=key)
            __row[key] = tmp[index]

        return __row

    def col_names(self):
        """Returns column naves or keys of table """
        return self.keys

    def get(self, key, value, operator, reindex=False) -> list:
        # ToDo: not very efficient, work on something a little faster
        """
        Return all rows where a key.value matches a specific value
        note that the logical operator is not sensitive to data type and will
        return anything that is true
        :param reindex: bool: first col as index can be re-indexed
        :param key: str: column name
        :param value: str: value where key.value matches based on operator
        :param operator: str: logical operator [>, <, >=, <=, !=, ==]
        :return: list: list of dictionary containing matching data
        """
        search_list, tmp = [], []
        col_data = self.col(key=key)

        # get data index where value equals
        for i in range(len(col_data)):
            tmp_val = col_data[i]
            if operator == '==':
                if tmp_val == value:
                    search_list.append(i)

            elif operator == '>':
                if tmp_val > value:
                    search_list.append(i)

            elif operator == '<':
                if tmp_val < value:
                    search_list.append(i)

            elif operator == '>=':
                if tmp_val >= value:
                    search_list.append(i)

            elif operator == '<=':
                if tmp_val <= value:
                    search_list.append(i)

            elif operator == '!=':
                if tmp_val != value:
                    search_list.append(i)

            else:
                raise ValueError(f'{operator} is not a valid operator')

        # return rows of equal data
        for i in search_list:
            tmp.append(self.row(index=i))

        if reindex:
            return self.re_index(data=tmp)

        return tmp

    def re_index(self, data):
        """Re-indexes data based on the first column as assumed id"""
        index_range = len(data)
        for i in range(index_range):
            data[i][self.keys[0]] = i + 1

        return data

    def delete(self):
        """Delete the table once all work has been completed """
        shutil.rmtree(f'stash/{self.table}')

    @staticmethod
    def un_stash():
        """Delete the ANApy stash system """
        shutil.rmtree('stash')
