import ast
import base64
import gzip
import os
import statistics

from anapy.utils import is_integer


class Analyse:
    """
    ANApy Analyse provides a set of simple analytical tools
    to help draw quick conclusions on stashed data for
    on-the-fly columnar level operations when manipulating data.

    data = dr.DataReader(data='data.json', format='json.gz').read()
    table = StashTable(data=data, table='data')
    table.save()

    table_ana = Analyse(table='data')  # stashed table name needs to be specified

    max = table_ana.max(col='0')
    print(max)

    table.un_stash()
    """

    def __init__(self, table):
        self.table = table

        self.cwd = os.getcwd() + '/stash/'

        # get keys from already existing table
        self.keys = [c for a, b, c in os.walk(self.cwd + self.table)][0]

    def __index_to_col(self, col):
        """Converts an index value to column name"""
        if is_integer(col):
            return self.keys[int(col)]
        return col

    def __bin_read(self, key):
        """Reads from binary ANApy file structure """
        try:
            with gzip.open(f'{self.cwd}/{self.table}/{key}', 'r') as f:
                dat = ast.literal_eval(base64.decodebytes(f.read()).decode())
                return dat
        except FileNotFoundError:
            raise ValueError(f'the column: "{key}" '
                             f'does not exist or has not been stashed')

    def max(self, col):
        """Returns max in column"""
        col = self.__index_to_col(col)
        data = self.__bin_read(key=col)

        try:
            return int(max(data))
        except ValueError:
            return max(data)

    def min(self, col):
        """Returns min in column"""
        col = self.__index_to_col(col)
        data = self.__bin_read(key=col)
        try:
            return int(min(data))
        except ValueError:
            return min(data)

    def mean(self, col):
        """Returns mean in column"""
        col = self.__index_to_col(col)
        data = self.__bin_read(key=col)

        return int(statistics.mean(list(map(int, data))))

    def median(self, col):
        """Returns median in column"""
        col = self.__index_to_col(col)
        data = self.__bin_read(key=col)

        try:
            return statistics.median(list(map(int, data)))
        except TypeError:
            raise ValueError('median can only accept numeric values')

    def mode(self, col):
        """Returns mode in column"""
        col = self.__index_to_col(col)
        data = self.__bin_read(key=col)

        try:
            return int(statistics.mode(data))
        except ValueError:
            statistics.mode(data)
