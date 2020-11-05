import ast
import base64
import gzip
import os
import shutil


def list_tables():
    """List current tables in stash"""
    return os.listdir('stash/')


def is_integer(x):
    """
    Checks if value x is integer and returns bool
    :param x: value to test
    :return: bool
    """
    try:
        int(x)
        return True
    except ValueError:
        return False


def get_type(x):
    """Consumes a value and determines its inherent data type"""
    if isinstance(x, bool):
        return bool

    if is_integer(x):
        return int

    if isinstance(x, float):
        return float

    if isinstance(x, complex):
        return complex

    if isinstance(x, bytes):
        return bytes

    return str


def list_type(lst, validate=False):
    """
    Simple list type test that returns the most
    common data type in a list or validates the
    types within a list
    :param lst: list: list of values to test
    :param validate: set validator which will raise an error
    :return: data type class
    """
    type_list = []
    for i in lst:
        type_list.append(get_type(i))

    if validate and len(set(type_list)) > 1:
        return ValueError('list contains multiple types '
                          'and can not infer a single type \n'
                          f'current data types: {set(type_list)}')
    return max(type_list, key=type_list.count)


def delete_tables(table):
    """
    Delete the table within the ANApy stash directory
    :param table: table to delete
    """
    try:
        shutil.rmtree(f'stash/{table}')
    except FileNotFoundError:
        raise FileNotFoundError(f'{table} is not a stashed table, '
                                'stashed tables are: \n'
                                f'{list_tables()}')


def binary_read(file):
    """
    Reads from gzip compressed file
    :param file: str: the file to read
    """
    with gzip.open(file, 'r') as f:
        return ast.literal_eval(base64.decodebytes(f.read()).decode())


def binary_write(file, data):
    """
    Writes to gzip compressed file
    :param file:
    :param data:
    :return:
    """
    with gzip.open(file, 'wb') as f:
        dat = base64.encodebytes(str(data).encode())
        f.write(dat)
