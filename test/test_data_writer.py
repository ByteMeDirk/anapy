import os
import unittest

import anapy.data_reader as dr
import anapy.data_writer as dw

cwd = os.getcwd()


class TestDataWriter(unittest.TestCase):

    # csv
    def test_write_csv_delim_1(self):
        """Write to csv with delim ,"""
        data = dr.DataReader(f_format='csv',
                             data=cwd + '/test/data/basic_csv.csv') \
            .read(delim=',')
        dw.write_csv(data=data, file='tmp.csv', delimiter=',')
        self.assertIs(os.path.isfile('tmp.csv'), True)
        os.remove('tmp.csv')

    def test_write_csv_delim_2(self):
        """Write to csv with delim ;"""
        data = dr.DataReader(f_format='csv',
                             data=cwd + '/test/data/basic_csv.csv') \
            .read(delim=',')
        dw.write_csv(data=data, file='tmp.csv', delimiter=';')
        self.assertIs(os.path.isfile('tmp.csv'), True)
        os.remove('tmp.csv')

    # json
    def test_write_json_allow_nan(self):
        """Write to json allowing nan"""
        data = dr.DataReader(f_format='csv',
                             data=cwd + '/test/data/basic_csv.csv') \
            .read(delim=',')
        dw.write_json(data=data, file='tmp.json', allow_nan=True)
        self.assertIs(os.path.isfile('tmp.json'), True)
        os.remove('tmp.json')

    def test_write_json_not_allow_nan(self):
        """Write to json not allowing nan"""
        data = dr.DataReader(f_format='csv',
                             data=cwd + '/test/data/basic_csv.csv') \
            .read(delim=',')
        dw.write_json(data=data, file='tmp.json', allow_nan=False)
        self.assertIs(os.path.isfile('tmp.json'), True)
        os.remove('tmp.json')

    def test_write_json_indent(self):
        """Write to json with indent"""
        data = dr.DataReader(f_format='csv',
                             data=cwd + '/test/data/basic_csv.csv') \
            .read(delim=',')
        dw.write_json(data=data, file='tmp.json', allow_nan=True, indent=4)
        self.assertIs(os.path.isfile('tmp.json'), True)
        os.remove('tmp.json')

    # yaml
    def test_write_yaml(self):
        """Write to yaml"""
        data = dr.DataReader(f_format='csv',
                             data=cwd + '/test/data/basic_csv.csv') \
            .read(delim=',')
        dw.write_yaml(data=data, file='tmp.yaml')
        self.assertIs(os.path.isfile('tmp.yaml'), True)
        os.remove('tmp.yaml')
