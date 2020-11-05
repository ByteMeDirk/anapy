import csv
import gzip
import json
import os
import re

import yaml


class DataReader:
    """
    The DataReader class in intended for a more
    low-level pythonic method of reading data from
    multiple serializations. In this case, all
    dependencies are based on the pre-provided modules
    that come with python 3.7 >
    """

    def __init__(self, data, f_format=None, **kwargs):
        """
        :param data: path to data
        :param f_format: extension of data NOTE: gzipped
        files should not have their inherent format suggested
        :param kwargs:
        """
        self.data = os.path.abspath(data)
        self.format = f_format
        self.compression = None

    def get_extension(self):
        """
        Simple process of getting extension
        from data absolute path string
        if extension is not provided, d_type
        expects a string 'csv', 'json' etc else
        exception is raised
        :return: str: data extension name
        """

        if self.format and 'gz' not in self.format:
            return self.format, None

        try:
            # if gzipped make sure to return the right extension
            if self.data.split('.')[-1] == 'gz':
                return self.data.split('.')[-2], 'gz'

            return self.data.split('.')[-1], None
        except IndexError:
            raise ValueError(f'population "file:{self.data}" '
                             'provided has no specified extension')

    def parse_csv(self, delim):
        """
        Consumes csv data file and returns dict
        :param delim: str: delimiter in csv file
        :return: dict object of data
        """
        if self.compression == 'gz':
            with gzip.open(self.data, 'rt') as gf:
                return [*csv.DictReader(gf,
                                        delimiter=delim,
                                        skipinitialspace=True)]

        with open(self.data) as f:
            return [{k: v for k, v in row.items()} for row in
                    csv.DictReader(f,
                                   delimiter=delim,
                                   skipinitialspace=True)]

    def parse_json(self):
        """
        Consumes json data file and returns dict
        :return: dict object of data
        """
        try:
            if self.compression == 'gz':
                with gzip.open(self.data, 'rt') as gf:
                    return json.load(gf)

            with open(self.data, 'rb') as f:
                return json.load(f)

        except json.decoder.JSONDecodeError:
            raise ValueError(f'data provided is not of type '
                             f'{self.format} or json is not valid')

    def parse_yaml(self):
        """
        Consumes yaml data file and returns dict
        :return: dict object of data
        """
        if self.compression == 'gz':
            with gzip.open(self.data, 'rt') as gf:
                return yaml.full_load(gf)

        with open(self.data) as f:
            return yaml.full_load(f)

    def parse_sql(self, sql_create):
        """
        Consumes sql insert file and returns dict
        :param sql_create: bool: set if sql file has table create method
        :return: dict object of data
        """
        if self.compression == 'gz':
            with gzip.open(self.data, 'rt') as gf:
                data, head, body, = [], [], []
                for statement in gf:
                    data.append(re.findall(r'\((.*?)\)', statement))
        else:
            with open(self.data) as f:
                data, head, body, count = [], [], [], 0
                for statement in f:
                    data.append(re.findall(r'\((.*?)\)', statement))

        # remove insert statement first
        if sql_create:
            data = [d for d in data if len(d) > 1]

        # get header and body list to zip
        for d in data:
            head.append(d[0].split(','))
            body.append(d[1].split(','))

        # inefficient but will do this for now:
        # remove whitespace
        head = [[s.strip() for s in sub] for sub in head]
        body = [[s.strip() for s in sub] for sub in body]
        # remove single quotes
        head = [[s.strip("'") for s in sub] for sub in head]
        body = [[s.strip("'") for s in sub] for sub in body]
        # replaced null with None
        body = [[s.replace('null', '') for s in sub] for sub in body]

        tmp = []
        for k, v in zip(head, body):
            tmp.append(dict(zip(k, v)))

        return tmp

    def read(self, delim=',', sql_create=False):
        """
        Get data, assumes serialization process
        and returns data object
        :param sql_create: str: specified if sql
        is being consumed that is basic insert
        on includes table creation
        :param delim: str: csv delimiter
        :return: data object
        """

        data_type, self.compression = self.get_extension()

        if data_type == 'csv':
            return self.parse_csv(delim)

        if data_type == 'json':
            return self.parse_json()

        if data_type in ['yaml', 'yml']:
            return self.parse_yaml()

        if data_type in ['sql']:
            return self.parse_sql(sql_create)

        raise ValueError('data provided has no extension specified \n'
                         'supported types: csv, json, yaml, sql')
