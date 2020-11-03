import os
import unittest

from anapy.data_reader import DataReader

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


class TestDataReader(unittest.TestCase):

    # Uncompressed Data Read
    # csv
    def test_csv_reader_type_format_true(self):
        """csv read with format specified"""
        tmp = DataReader(data=data_paths['csv'],
                         format='csv').read(delim=',')
        self.assertIs(type(tmp) == list, True)

    def test_csv_reader_type_format_false(self):
        """csv read with format unspecified"""
        tmp = DataReader(data=data_paths['csv']).read(delim=',')
        self.assertIs(type(tmp) == list, True)

    # json
    def test_json_reader_type_format_true(self):
        """json read with format specified"""
        tmp = DataReader(data=data_paths['json_arr'],
                         format='json').read()
        self.assertIs(type(tmp) == list, True)

    def test_json_reader_type_format_false(self):
        """json read with format unspecified"""
        tmp = DataReader(data=data_paths['json_arr']).read()
        self.assertIs(type(tmp) == list, True)

    # yaml
    def test_yaml_reader_type_format_true(self):
        """yaml read with format specified"""
        tmp = DataReader(data=data_paths['yaml'],
                         format='yaml').read()
        self.assertIs(type(tmp) == list, True)

    def test_yaml_reader_type_format_false(self):
        """yaml read with format unspecified"""
        tmp = DataReader(data=data_paths['yaml']).read()
        self.assertIs(type(tmp) == list, True)

    # sql insert
    def test_sql_insert_reader_type_format_true(self):
        """sql read with format specified"""
        tmp = DataReader(data=data_paths['sql'],
                         format='sql') \
            .read(sql_create=False)
        self.assertIs(type(tmp) == list, True)

    def test_sql_insert_reader_type_format_false(self):
        """sql read with format unspecified"""
        tmp = DataReader(data=data_paths['sql']) \
            .read(sql_create=False)
        self.assertIs(type(tmp) == list, True)

    # sql create
    def test_sql_create_reader_type_format_true(self):
        """sql read with format specified"""
        tmp = DataReader(data=data_paths['sql_cr'],
                         format='sql') \
            .read(sql_create=True)
        self.assertIs(type(tmp) == list, True)

    def test_sql_create_reader_type_format_false(self):
        """sql read with format unspecified"""
        tmp = DataReader(data=data_paths['sql_cr']) \
            .read(sql_create=True)
        self.assertIs(type(tmp) == list, True)

    # Compressed Data Read
    # csv
    def test_comp_csv_reader_type_format_true(self):
        """csv read with format specified"""
        tmp = DataReader(data=data_paths['csv_gz'],
                         format='csv.gz') \
            .read(delim=',')
        self.assertIs(type(tmp) == list, True)

    def test_comp_csv_reader_type_format_false(self):
        """csv read with format unspecified"""
        tmp = DataReader(data=data_paths['csv_gz']) \
            .read(delim=',')
        self.assertIs(type(tmp) == list, True)

    # json
    def test_comp_json_reader_type_format_true(self):
        """json read with format specified"""
        tmp = DataReader(data=data_paths['json_gz'],
                         format='json.gz') \
            .read()
        self.assertIs(type(tmp) == list, True)

    def test_comp_json_reader_type_format_false(self):
        """json read with format unspecified"""
        tmp = DataReader(data=data_paths['json_gz']) \
            .read()
        self.assertIs(type(tmp) == list, True)

    # yaml
    def test_comp_yaml_reader_type_format_true(self):
        """yaml read with format specified"""
        tmp = DataReader(data=data_paths['yaml_gz'],
                         format='yaml.gz') \
            .read()
        self.assertIs(type(tmp) == list, True)

    def test_comp_yaml_reader_type_format_false(self):
        """yaml read with format unspecified"""
        tmp = DataReader(data=data_paths['yaml_gz']) \
            .read()
        self.assertIs(type(tmp) == list, True)

    # sql
    def test_comp_sql_insert_reader_type_format_true(self):
        """sql read with format specified"""
        tmp = DataReader(data=data_paths['sql_gz'],
                         format='sql.gz') \
            .read(sql_create=False)
        self.assertIs(type(tmp) == list, True)

    def test_comp_sql_insert_reader_type_format_false(self):
        """sql read with format unspecified"""
        tmp = DataReader(data=data_paths['sql_gz']) \
            .read(sql_create=False)
        self.assertIs(type(tmp) == list, True)
