import os
import unittest

import anapy.data_reader as dr
import anapy.data_writer as dw
import anapy.stash as st

cwd = os.getcwd()

data_paths = {
    'csv': os.path.abspath(cwd + '/test/data/basic_csv.csv'),
    'csv_gz': os.path.abspath(cwd + '/test/data/basic_csv.csv.gz'),
    'yaml': os.path.abspath(cwd + '/test/data/basic_yaml.yaml'),
    'yaml_gz': os.path.abspath(cwd + '/test/data/basic_yaml.yaml.gz'),
    'json_arr': os.path.abspath(cwd + '/test/data/json_array.json'),
    'json_gz': os.path.abspath(cwd + '/test/data/json_array.json.gz'),
    'sql_cr': os.path.abspath(cwd + '/test/data/sql_create.sql'),
    'sql': os.path.abspath(cwd + '/test/data/sql_insert.sql'),
    'sql_gz': os.path.abspath(cwd + '/test/data/sql_insert.sql.gz')
}


class TestCoreUseCase(unittest.TestCase):
    def test_use_case_csv_csv(self):
        """Simple use case using core tools for reading, computing and writing"""
        raised = False

        try:
            data = dr.DataReader(data=data_paths['csv'], f_format='csv').read()
            table = st.StashTable(data=data, table='data')
            table.save()

            col_names = table.col_names()
            first_row = table.row(index=0)
            first_col = table.col(key='id')

            subset = table.get(key='gender', value='Female', operator='==', reindex=True)

            dw.write_csv(data=subset, file='subset.csv', header=True)
            dw.write_csv(data=subset, file='subset.csv', header=True, quoting='all')
            dw.write_csv(data=subset, file='subset.csv', header=True, quoting='minimal')
            dw.write_csv(data=subset, file='subset.csv', header=True, quoting='nonumeric')

            table.un_stash()

            os.remove('subset.csv')
        except:
            raised = True

        self.assertIs(raised, False)

    def test_use_case_csv_json(self):
        """Simple use case using core tools for reading, computing and writing"""
        raised = False

        try:
            data = dr.DataReader(data=data_paths['csv'], f_format='csv').read()
            table = st.StashTable(data=data, table='data')
            table.save()

            col_names = table.col_names()
            first_row = table.row(index=0)
            first_col = table.col(key='id')

            subset = table.get(key='gender', value='Female', operator='==', reindex=True)

            dw.write_json(data=subset, file='subset.json', allow_nan=False, sort_keys=False)
            dw.write_json(data=subset, file='subset.json', allow_nan=True, sort_keys=True)

            table.un_stash()

            os.remove('subset.json')
        except:
            raised = True

        self.assertIs(raised, False)

    def test_use_case_csv_yaml(self):
        """Simple use case using core tools for reading, computing and writing"""
        raised = False

        try:
            data = dr.DataReader(data=data_paths['csv'], f_format='csv').read()
            table = st.StashTable(data=data, table='data')
            table.save()

            col_names = table.col_names()
            first_row = table.row(index=0)
            first_col = table.col(key='id')

            subset = table.get(key='gender', value='Female', operator='==', reindex=True)

            dw.write_yaml(data=subset, file='subset.yaml')

            table.un_stash()

            os.remove('subset.yaml')
        except:
            raised = True

        self.assertIs(raised, False)

    def test_use_case_json_csv(self):
        """Simple use case using core tools for reading, computing and writing"""
        raised = False

        try:
            data = dr.DataReader(data=data_paths['json_arr'], f_format='json').read()
            table = st.StashTable(data=data, table='data')
            table.save()

            col_names = table.col_names()
            first_row = table.row(index=0)
            first_col = table.col(key='id')

            subset = table.get(key='gender', value='Female', operator='==', reindex=True)

            dw.write_csv(data=subset, file='subset.csv', header=True)
            dw.write_csv(data=subset, file='subset.csv', header=True, quoting='all')
            dw.write_csv(data=subset, file='subset.csv', header=True, quoting='minimal')
            dw.write_csv(data=subset, file='subset.csv', header=True, quoting='nonumeric')

            table.un_stash()

            os.remove('subset.csv')
        except:
            raised = True

        self.assertIs(raised, False)

    def test_use_case_json_json(self):
        """Simple use case using core tools for reading, computing and writing"""
        raised = False

        try:
            data = dr.DataReader(data=data_paths['json_arr'], f_format='json').read()
            table = st.StashTable(data=data, table='data')
            table.save()

            col_names = table.col_names()
            first_row = table.row(index=0)
            first_col = table.col(key='id')

            subset = table.get(key='gender', value='Female', operator='==', reindex=True)

            dw.write_json(data=subset, file='subset.json', allow_nan=False, sort_keys=False)
            dw.write_json(data=subset, file='subset.json', allow_nan=True, sort_keys=True)

            table.un_stash()

            os.remove('subset.json')
        except:
            raised = True

        self.assertIs(raised, False)

    def test_use_case_json_yaml(self):
        """Simple use case using core tools for reading, computing and writing"""
        raised = False

        try:
            data = dr.DataReader(data=data_paths['json_arr'], f_format='json').read()
            table = st.StashTable(data=data, table='data')
            table.save()

            col_names = table.col_names()
            first_row = table.row(index=0)
            first_col = table.col(key='id')

            subset = table.get(key='gender', value='Female', operator='==', reindex=True)

            dw.write_yaml(data=subset, file='subset.yaml')

            table.un_stash()

            os.remove('subset.yaml')
        except:
            raised = True

        self.assertIs(raised, False)

    def test_use_case_yaml_csv(self):
        """Simple use case using core tools for reading, computing and writing"""
        raised = False

        try:
            data = dr.DataReader(data=data_paths['yaml'], f_format='yaml').read()
            table = st.StashTable(data=data, table='data')
            table.save()

            col_names = table.col_names()
            first_row = table.row(index=0)
            first_col = table.col(key='id')

            subset = table.get(key='gender', value='Female', operator='==', reindex=True)

            dw.write_csv(data=subset, file='subset.csv', header=True)
            dw.write_csv(data=subset, file='subset.csv', header=True, quoting='all')
            dw.write_csv(data=subset, file='subset.csv', header=True, quoting='minimal')
            dw.write_csv(data=subset, file='subset.csv', header=True, quoting='nonumeric')

            table.un_stash()

            os.remove('subset.csv')
        except:
            raised = True

        self.assertIs(raised, False)

    def test_use_case_yaml_json(self):
        """Simple use case using core tools for reading, computing and writing"""
        raised = False

        try:
            data = dr.DataReader(data=data_paths['yaml'], f_format='yaml').read()
            table = st.StashTable(data=data, table='data')
            table.save()

            col_names = table.col_names()
            first_row = table.row(index=0)
            first_col = table.col(key='id')

            subset = table.get(key='gender', value='Female', operator='==', reindex=True)

            dw.write_json(data=subset, file='subset.json', allow_nan=False, sort_keys=False)
            dw.write_json(data=subset, file='subset.json', allow_nan=True, sort_keys=True)

            table.un_stash()

            os.remove('subset.json')
        except:
            raised = True

        self.assertIs(raised, False)

    def test_use_case_yaml_yaml(self):
        """Simple use case using core tools for reading, computing and writing"""
        raised = False

        try:
            data = dr.DataReader(data=data_paths['yaml'], f_format='yaml').read()
            table = st.StashTable(data=data, table='data')
            table.save()

            col_names = table.col_names()
            first_row = table.row(index=0)
            first_col = table.col(key='id')

            subset = table.get(key='gender', value='Female', operator='==', reindex=True)

            dw.write_yaml(data=subset, file='subset.yaml')

            table.un_stash()

            os.remove('subset.yaml')
        except:
            raised = True

        self.assertIs(raised, False)

    def test_use_case_sql_csv(self):
        """Simple use case using core tools for reading, computing and writing"""
        raised = False

        try:
            data = dr.DataReader(data=data_paths['sql'], f_format='sql').read()
            table = st.StashTable(data=data, table='data')
            table.save()

            col_names = table.col_names()
            first_row = table.row(index=0)
            first_col = table.col(key='id')

            subset = table.get(key='gender', value='Female', operator='==', reindex=True)

            dw.write_csv(data=subset, file='subset.csv', header=True)
            dw.write_csv(data=subset, file='subset.csv', header=True, quoting='all')
            dw.write_csv(data=subset, file='subset.csv', header=True, quoting='minimal')
            dw.write_csv(data=subset, file='subset.csv', header=True, quoting='nonumeric')

            table.un_stash()

            os.remove('subset.csv')
        except:
            raised = True

        self.assertIs(raised, False)

    def test_use_case_sql_json(self):
        """Simple use case using core tools for reading, computing and writing"""
        raised = False

        try:
            data = dr.DataReader(data=data_paths['sql'], f_format='sql').read()
            table = st.StashTable(data=data, table='data')
            table.save()

            col_names = table.col_names()
            first_row = table.row(index=0)
            first_col = table.col(key='id')

            subset = table.get(key='gender', value='Female', operator='==', reindex=True)

            dw.write_json(data=subset, file='subset.json', allow_nan=False, sort_keys=False)
            dw.write_json(data=subset, file='subset.json', allow_nan=True, sort_keys=True)

            table.un_stash()

            os.remove('subset.json')
        except:
            raised = True

        self.assertIs(raised, False)

    def test_use_case_sql_yaml(self):
        """Simple use case using core tools for reading, computing and writing"""
        raised = False

        try:
            data = dr.DataReader(data=data_paths['sql'], f_format='sql').read()
            table = st.StashTable(data=data, table='data')
            table.save()

            col_names = table.col_names()
            first_row = table.row(index=0)
            first_col = table.col(key='id')

            subset = table.get(key='gender', value='Female', operator='==', reindex=True)

            dw.write_yaml(data=subset, file='subset.yaml')

            table.un_stash()

            os.remove('subset.yaml')
        except:
            raised = True

        self.assertIs(raised, False)
