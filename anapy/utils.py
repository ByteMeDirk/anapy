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
