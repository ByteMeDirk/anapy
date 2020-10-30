import csv
import os
import json
import yaml


class DataWriter:
    """
    The DataReader class in intended for a more low-level pythonic method of reading data from
    multiple serializations. In this case, all dependencies are based on the pre-provided modules
    that come with python 3.7 >
    """

    def __init__(self, data, file, **kwargs):
        """
        :param file: data object
        :param d_type: format to write data to
        :param kwargs:
        """
        self.file = file
        self.data = data

    @staticmethod
    def csv_quote(quoting):
        try:
            if quoting == 'all':
                return csv.QUOTE_ALL
            elif quoting == 'minimal':
                return csv.QUOTE_MINIMAL
            elif quoting == 'nonnumeric':
                return csv.QUOTE_NONNUMERIC
            else:
                return csv.QUOTE_NONE
        except ValueError:
            raise ValueError('only quiting params specified are [all, minimal, nonumeric] otherwise none')


    def write(self, format='csv', **kwargs):
        if format == 'csv':
            col_names = [i for i in self.data[0]]

            with open(self.file, 'w') as f:
                writer = csv.DictWriter(f, fieldnames=col_names,
                                        delimiter=kwargs['delimiter'],
                                        quoting=self.csv_quote(kwargs['quoting']))

                if kwargs['header']:
                    writer.writeheader()

                for data in self.data:
                    writer.writerow(data)
        elif format == 'json':
            pass
        elif format == 'yaml':
            pass
        else:
            raise ValueError('please specify a data format to write to')
