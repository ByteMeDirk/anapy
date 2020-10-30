import csv
import json

import yaml


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


def strip_dict(d):
    return {key: strip_dict(value) if isinstance(value, dict) else value.strip() for key, value in d.items()}


def write_csv(delimiter=',', quoting=None, header=True, **kwargs):
    col_names = [i for i in kwargs['data'][0]]
    with open(kwargs['file'], 'w') as f:
        writer = csv.DictWriter(f, fieldnames=col_names,
                                delimiter=delimiter,
                                quoting=csv_quote(quoting))
        if header:
            writer.writeheader()

        for data in kwargs['data']:
            # writer.writerow(strip_dict(data))
            writer.writerow(data)

def write_json(indent=None, allow_nan=True, sort_keys=True, **kwargs):
    with open(kwargs['file'], 'w') as f:
        json.dump(kwargs['data'], fp=f, indent=indent, allow_nan=allow_nan, sort_keys=sort_keys)


def write_yaml(**kwargs):
    with open(kwargs['file'], 'w') as f:
        yaml.dump(kwargs['data'], f)
