import csv
import os
import json
import yaml


class DataReader:
    """
    The DataReader class in intended for a more low-level pythonic method of reading data from
    multiple serializations. In this case, all dependencies are based on the pre-provided modules
    that come with python 3.7 >
    """

    def __init__(self, data, d_type=None, **kwargs):
        """
        :param data: path to data
        :param d_type: extension of data
        :param kwargs:
        """
        self.data = os.path.abspath(data)
        self.d_type = d_type

    def get_extension(self):
        """
        simple process of getting extension from data absolute path string
        if extension is not provided, d_type expects a string 'csv', 'json' etc else exception is raised
        :return: str: data extension name
        """
        if self.d_type:
            return self.d_type
        else:
            try:
                return self.data.split('.')[-1]
            except IndexError:
                raise ValueError(f'population "file:{self.data}" provided has no specified extension')

    def parse_csv(self, delim):
        """
        consumes csv data file and returns dict
        :param delim: str: delimiter in csv file
        :return: dict object of data
        """
        with open(self.data) as f:
            return [{k: v for k, v in row.items()} for row in csv.DictReader(f, delimiter=delim, skipinitialspace=True)]

    def parse_json(self):
        """
        consumes json data file and returns dict
        :return: dict object of data
        """
        try:
            with open(self.data, 'rb') as f:
                return json.load(f)
        except json.decoder.JSONDecodeError:
            raise ValueError(f'data provided is not of type {self.d_type}')

    def parse_yaml(self):
        """
        consumes yaml data file and returns dict
        :return: dict object of data
        """
        with open(self.data) as f:
            return yaml.full_load(f)

    def read(self, delim=','):
        """
        get data, assumes serialization process and returns data object
        :param delim: str: csv delimiter
        :return: data object
        """
        data_type = self.get_extension()
        if data_type == 'csv':
            return self.parse_csv(delim)
        elif data_type == 'json':
            return self.parse_json()
        elif data_type in ['yaml', 'yml']:
            return self.parse_yaml()
        else:
            raise ValueError('data provided has no extension specified \n'
                             'supported types: csv, json')
