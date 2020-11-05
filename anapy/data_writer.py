import csv
import json

import yaml


def csv_quote(quoting):
    """Define quoting params for csv writing"""
    try:
        if quoting == 'all':
            return csv.QUOTE_ALL

        if quoting == 'minimal':
            return csv.QUOTE_MINIMAL

        if quoting == 'nonnumeric':
            return csv.QUOTE_NONNUMERIC

        return csv.QUOTE_NONE

    except ValueError:
        raise ValueError('only quiting params specified are '
                         '[all, minimal, nonumeric] otherwise none')


def strip_dict(d):
    """Cleans up dictionary obtained from a messy file """
    return {key: strip_dict(value) if isinstance(value, dict) else value.strip()
            for key, value in d.items()}


def write_csv(delimiter=',', quoting=None, header=True, **kwargs):
    """
    Write ANApy consumed data to csv file
    :param delimiter: str: csv delimiter
    :param quoting: str: quiting level of data [all, minimal, nonumeric] default none
    :param header: bool: header true or false
    :param file: file to write csv to
    :param data: data to consume
    """
    with open(kwargs['file'], 'w') as f:
        print(kwargs['data'])
        writer = csv.DictWriter(f,
                                fieldnames=[*kwargs['data'][0]],
                                delimiter=delimiter,
                                quoting=csv_quote(quoting))
        if header:
            writer.writeheader()

        for data in kwargs['data']:
            writer.writerow(data)


def write_json(indent=None, allow_nan=True, sort_keys=True, **kwargs):
    """
    Write ANApy consumed data to json file
    :param indent: int: json indent level, default is compact
    :param allow_nan: bool: allow nan values to be written
    :param sort_keys: boo: sort keys
    :param file: file to write csv to
    :param data: data to consume
    """
    with open(kwargs['file'], 'w') as f:
        json.dump(kwargs['data'],
                  fp=f,
                  indent=indent,
                  allow_nan=allow_nan,
                  sort_keys=sort_keys)


def write_yaml(**kwargs):
    """
    Write ANApy consumed data to yaml file
    :param file: file to write csv to
    :param data: data to consume
    """
    with open(kwargs['file'], 'w') as f:
        yaml.dump(kwargs['data'], f)
