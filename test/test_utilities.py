import os
import unittest

import anapy.data_reader as dr
import anapy.stash as st
from anapy import utils

cwd = os.getcwd()


class TestStash(unittest.TestCase):

    @staticmethod
    def get_data():
        """Get mock data for stash"""
        _dir = cwd + '/test/data/basic_csv.csv'
        return dr.DataReader(f_format='csv',
                             data=_dir).read(delim=',')

    def test_list_tables(self):
        """Tests the list tables util method"""
        data = self.get_data()
        table = st.StashTable(data=data, table='basic')
        table.save()
        self.assertEqual(utils.list_tables(), ['basic'])
        table.delete()

    def test_is_integer(self):
        """Tests the is integer util method"""
        self.assertIs(utils.is_integer('1'), True)

    def test_get_type_int(self):
        """Tests the get type for int util method"""
        self.assertEqual(utils.get_type('55'), int)

    def test_get_type_bool(self):
        """Tests the get type for bool util method"""
        self.assertEqual(utils.get_type(True), bool)

    def test_get_type_string(self):
        """Tests the get type for str util method"""
        self.assertEqual(utils.get_type('string'), str)

    def test_list_type_int(self):
        """Tests the list type for int util method"""
        self.assertEqual(utils.list_type([1, 2, 3, 4, 5, 6, 7]), int)

    def test_list_type_string(self):
        """Tests the list type for str util method"""
        self.assertEqual(utils.list_type(['a', 'b', 'c', 'd']), str)

    def test_list_type_bool(self):
        """Tests the list type for bool util method"""
        self.assertEqual(utils.list_type([True, True, False, False]), bool)
