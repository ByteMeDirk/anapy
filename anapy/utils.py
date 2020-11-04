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
    Delete the table within the stash directory
    :param table: table to delete
    """
    try:
        shutil.rmtree(f'stash/{table}')
    except FileNotFoundError:
        raise FileNotFoundError(f'{table} is not a stashed table, '
                                'stashed tables are: \n'
                                f'{list_tables()}')
