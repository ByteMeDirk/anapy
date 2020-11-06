import os
import unittest

import anapy.data_reader as dr
import anapy.stash as st

cwd = os.getcwd()


class TestStash(unittest.TestCase):
    """Test anapy.stash"""

    @staticmethod
    def get_data():
        """Get mock data for stash"""
        _dir = cwd + '/test/data/basic_csv.csv'
        return dr.DataReader(f_format='csv',
                             data=_dir).read(delim=',')

    def test_stash_table_root(self):
        """Assert root stash dir exisits"""
        data = self.get_data()
        table = st.StashTable(data=data, table='basic')
        table.save()
        self.assertTrue(os.path.exists('stash'))
        table.delete()

    def test_stash_table(self):
        """Assert table dir exists"""
        data = self.get_data()
        table = st.StashTable(data=data, table='basic')
        table.save()
        self.assertTrue(os.path.exists('stash/basic'))
        table.delete()

    def test_stash_table_content(self):
        """Assert table sub dirs exists adn test structure"""
        data = self.get_data()
        table = st.StashTable(data=data, table='basic')
        table.save()

        cols = table.col_names()

        for i in cols:
            self.assertTrue(os.path.exists(f'stash/basic/{i}'))

        table.delete()

    def test_stash_table_remove(self):
        """Assert table dir exists"""
        data = self.get_data()
        table = st.StashTable(data=data, table='basic')
        table.save()
        table.delete()

        self.assertEqual(os.path.exists('stash/basic'), False)

    def test_col(self):
        """Ensure col method works"""
        data = self.get_data()
        table = st.StashTable(data=data, table='basic')
        table.save()

        tmp = table.col(key='gender')

        self.assertGreater(len(tmp), 1)

    def test_row(self):
        """Ensure row method works"""
        data = self.get_data()
        table = st.StashTable(data=data, table='basic')
        table.save()

        tmp = table.row(index=0)

        self.assertGreater(len(tmp), 1)

    def test_get(self):
        """Ensure row method works"""
        data = self.get_data()
        table = st.StashTable(data=data, table='basic')
        table.save()

        tmp = table.get(key='gender', value='Female', operator='==')

        self.assertGreater(len(tmp), 1)
