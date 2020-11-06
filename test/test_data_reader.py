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
    """Test anapy.data_reader"""

    # Uncompressed Data Read
    # csv
    def test_csv_reader_type_format_true(self):
        """Csv read with format specified"""
        tmp = DataReader(data=data_paths['csv'],
                         f_format='csv').read(delim=',')
        self.assertIs(type(tmp), list)

    def test_csv_reader_type_format_false(self):
        """Csv read with format unspecified"""
        tmp = DataReader(data=data_paths['csv']).read(delim=',')
        self.assertIs(type(tmp), list)

    # json
    def test_json_reader_type_format_true(self):
        """Json read with format specified"""
        tmp = DataReader(data=data_paths['json_arr'],
                         f_format='json').read()
        self.assertIs(type(tmp), list)

    def test_json_reader_type_format_false(self):
        """Json read with format unspecified"""
        tmp = DataReader(data=data_paths['json_arr']).read()
        self.assertIs(type(tmp), list)

    # yaml
    def test_yaml_reader_type_format_true(self):
        """Yaml read with format specified"""
        tmp = DataReader(data=data_paths['yaml'],
                         f_format='yaml').read()
        self.assertIs(type(tmp), list)

    def test_yaml_reader_type_format_false(self):
        """Yaml read with format unspecified"""
        tmp = DataReader(data=data_paths['yaml']).read()
        self.assertIs(type(tmp), list)

    # sql insert
    def test_sql_insert_reader_type_format_true(self):
        """Sql read with format specified"""
        tmp = DataReader(data=data_paths['sql'],
                         f_format='sql') \
            .read(sql_create=False)
        self.assertIs(type(tmp), list)

    def test_sql_insert_reader_type_format_false(self):
        """Sql read with format unspecified"""
        tmp = DataReader(data=data_paths['sql']) \
            .read(sql_create=False)
        self.assertIs(type(tmp), list)

    # sql create
    def test_sql_create_reader_type_format_true(self):
        """Sql read with format specified"""
        tmp = DataReader(data=data_paths['sql_cr'],
                         f_format='sql') \
            .read(sql_create=True)
        self.assertIs(type(tmp), list)

    def test_sql_create_reader_type_format_false(self):
        """Sql read with format unspecified"""
        tmp = DataReader(data=data_paths['sql_cr']) \
            .read(sql_create=True)
        self.assertIs(type(tmp), list)

    # Compressed Data Read
    # csv
    def test_comp_csv_reader_type_format_true(self):
        """Csv read with format specified"""
        tmp = DataReader(data=data_paths['csv_gz'],
                         f_format='csv.gz') \
            .read(delim=',')
        self.assertIs(type(tmp), list)

    def test_comp_csv_reader_type_format_false(self):
        """Csv read with format unspecified"""
        tmp = DataReader(data=data_paths['csv_gz']) \
            .read(delim=',')
        self.assertIs(type(tmp), list)

    # json
    def test_comp_json_reader_type_format_true(self):
        """Json read with format specified"""
        tmp = DataReader(data=data_paths['json_gz'],
                         f_format='json.gz') \
            .read()
        self.assertIs(type(tmp), list)

    def test_comp_json_reader_type_format_false(self):
        """Json read with format unspecified"""
        tmp = DataReader(data=data_paths['json_gz']) \
            .read()
        self.assertIs(type(tmp), list)

    # yaml
    def test_comp_yaml_reader_type_format_true(self):
        """Yaml read with format specified"""
        tmp = DataReader(data=data_paths['yaml_gz'],
                         f_format='yaml.gz') \
            .read()
        self.assertIs(type(tmp), list)

    def test_comp_yaml_reader_type_format_false(self):
        """Yaml read with format unspecified"""
        tmp = DataReader(data=data_paths['yaml_gz']) \
            .read()
        self.assertIs(type(tmp), list)

    # sql
    def test_comp_sql_insert_reader_type_format_true(self):
        """Sql read with format specified"""
        tmp = DataReader(data=data_paths['sql_gz'],
                         f_format='sql.gz') \
            .read(sql_create=False)
        self.assertIs(type(tmp), list)

    def test_comp_sql_insert_reader_type_format_false(self):
        """Sql read with format unspecified"""
        tmp = DataReader(data=data_paths['sql_gz']) \
            .read(sql_create=False)
        self.assertIs(type(tmp), list)
