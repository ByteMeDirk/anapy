import unittest
from anapy.data_reader import DataReader
import os

data_paths = {
    'csv': os.path.abspath('../tests/data/MOCK_DATA.csv'),
    'json': os.path.abspath('../tests/data/MOCK_DATA.json'),
    'yaml': os.path.abspath('../tests/data/MOCK_DATA.yaml'),
    'txt': os.path.abspath('../tests/data/MOCK_DATA')
}


class TestDataReader(unittest.TestCase):

    # csv
    def test_csv_reader_type(self):
        tmp = DataReader(data=data_paths['csv']).read()
        self.assertTrue(type(tmp) == list)

    def test_csv_reader_len(self):
        tmp = DataReader(data=data_paths['csv']).read()
        self.assertTrue(len(tmp) == 1000)

    # json
    def test_json_reader_type(self):
        tmp = DataReader(data=data_paths['json']).read()
        self.assertTrue(type(tmp) == list)

    def test_json_reader_len(self):
        tmp = DataReader(data=data_paths['json']).read()
        self.assertTrue(len(tmp) == 1000)

    # yaml
    def test_yaml_reader_type(self):
        tmp = DataReader(data=data_paths['yaml']).read()
        self.assertTrue(type(tmp) == list)

    def test_yaml_reader_len(self):
        tmp = DataReader(data=data_paths['yaml']).read()
        self.assertTrue(len(tmp) == 1000)

    # text
    def test_text_reader_type(self):
        tmp = DataReader(data=data_paths['txt'], d_type='csv').read()
        self.assertTrue(type(tmp) == list)

    def test_text_reader_len(self):
        tmp = DataReader(data=data_paths['txt'], d_type='csv').read()
        self.assertTrue(len(tmp) == 1000)
