import os
import unittest

import anapy.stash as st
from anapy import analyse as ana
from anapy import data_reader as dr

cwd = os.getcwd()


class TestAnalyze(unittest.TestCase):
    """Test anapy.analyse"""

    @staticmethod
    def get_data():
        """Get mock data for stash"""
        _dir = cwd + '/test/data/basic_csv.csv'
        return dr.DataReader(f_format='csv',
                             data=_dir).read(delim=',')

    def test_max(self):
        """Test min returns highest val in id"""
        data = self.get_data()
        table = st.StashTable(data=data, table='basic')
        table.save()

        ana_table = ana.Analyse('basic')
        tmp = ana_table.max('id')

        self.assertEqual(tmp, 999)
        table.delete()

    def test_min(self):
        """Test min returns lowest val in id"""
        data = self.get_data()
        table = st.StashTable(data=data, table='basic')
        table.save()

        ana_table = ana.Analyse('basic')
        tmp = ana_table.min('id')

        self.assertEqual(tmp, 1)
        table.delete()

    def test_mean(self):
        """Test min returns highest val in id"""
        data = self.get_data()
        table = st.StashTable(data=data, table='basic')
        table.save()

        ana_table = ana.Analyse('basic')
        tmp = ana_table.mean('id')

        self.assertEqual(round(tmp), 500)
        table.delete()

    def test_mode(self):
        """Test min returns highest val in id"""
        data = self.get_data()
        table = st.StashTable(data=data, table='basic')
        table.save()

        ana_table = ana.Analyse('basic')
        tmp = ana_table.mode('id')

        self.assertEqual(tmp, 1)
        table.delete()

    def test_median(self):
        """Test min returns highest val in id"""
        data = self.get_data()
        table = st.StashTable(data=data, table='basic')
        table.save()

        ana_table = ana.Analyse('basic')
        tmp = ana_table.median('id')

        self.assertEqual(round(tmp), 500)
        table.delete()
