import unittest
import anapy.data_reader as dr
import anapy.data_writer as dw
import anapy.stash as st
import os

cwd = os.getcwd()


class TestStash(unittest.TestCase):

    @staticmethod
    def get_data():
        """get mock data for stash"""
        _dir = cwd + '/test/data/basic_csv.csv'
        return dr.DataReader(format='csv',
                             data=_dir).read(delim=',')

    def test_stash_table_root(self):
        """assert root stash dir exisits"""
        data = self.get_data()
        table = st.StashTable(data=data, table='basic')
        table.save()
        self.assertTrue(os.path.exists('stash'))
        table.delete()

    def test_stash_table(self):
        """assert table dir exists"""
        data = self.get_data()
        table = st.StashTable(data=data, table='basic')
        table.save()
        self.assertTrue(os.path.exists('stash/basic'))
        table.delete()

    def test_stash_table_content(self):
        """assert table sub dirs exists adn test structure"""
        data = self.get_data()
        table = st.StashTable(data=data, table='basic')
        table.save()

        cols = table.col_names()

        for i in cols:
            self.assertTrue(os.path.exists(f'stash/basic/{i}'))

        table.delete()

    def test_stash_table_remove(self):
        """assert table dir exists"""
        data = self.get_data()
        table = st.StashTable(data=data, table='basic')
        table.save()
        table.delete()

        self.assertEqual(os.path.exists('stash/basic'), False)

    def test_col(self):
        """ensure col method works"""
        data = self.get_data()
        table = st.StashTable(data=data, table='basic')
        table.save()

        tmp = table.col(key='gender')

        self.assertGreater(len(tmp), 1)

    def test_row(self):
        """ensure row method works"""
        data = self.get_data()
        table = st.StashTable(data=data, table='basic')
        table.save()

        tmp = table.row(index=0)

        self.assertGreater(len(tmp), 1)

    def test_get(self):
        """ensure row method works"""
        data = self.get_data()
        table = st.StashTable(data=data, table='basic')
        table.save()

        tmp = table.get(key='gender', value='Female', operator='==')

        self.assertGreater(len(tmp), 1)
