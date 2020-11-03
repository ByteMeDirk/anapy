.. image:: static/logo.png

----------------------

anapy is the beginning of a simplified universal data manipulation library for handling all forms of data

.. image:: https://img.shields.io/pypi/v/anapy?style=for-the-badge
.. image:: https://img.shields.io/github/license/dirkscgm/anapy?style=for-the-badge
.. image:: https://img.shields.io/github/languages/top/dirkscgm/anapy?style=for-the-badge

----------------------

.. image:: https://deepsource.io/gh/DirksCGM/anapy.svg/?label=active+issues&show_trend=true    :target: https://deepsource.io/gh/DirksCGM/anapy/?ref=repository-badge
.. image:: https://deepsource.io/gh/DirksCGM/anapy.svg/?label=resolved+issues&show_trend=true    :target: https://deepsource.io/gh/DirksCGM/anapy/?ref=repository-badge

What is Anapy?
**********************

Anapy is a compact data serialization and manipulation tool. It is still WIP though the intention is to have a 
lightweight tool that can read and write to multiple data formats, as well as perform base data manipulation
tasks for Data specialists who need a quick solution for a simple problem. 

Reading Data
#####################

ANApy has a basic reader that currently supports csv, json, yaml and sql-inserts.

.. code-block:: python

    from anapy import data_reader as dr
    data = dr.DataReader(data='data.csv', d_type='csv').read(delim=',')
    data = dr.DataReader(data='data.json', d_type='json')
    data = dr.DataReader(data='data.yaml', d_type='yaml')
    data = dr.DataReader(data='data.sql', d_type='sql').read(sql_create=False)

Writing Data
#######################

Once data has been consumed, it can be written in various formats:

.. code-block:: python

    import anapy.data_writer as dw
    dw.write_csv(file='data.csv', data=data, quoting='minimal', header=True)
    dw.write_yaml(file='data.yaml', data=data)
    dw.write_json(file='data.json', data=data, allow_nan=True, sort_keys=False)


Stashing Data
#######################

ANApy is currently having a stashing process developed designed to temporarily
store and work with data on a columnar level. This means general querying of data to
new subsets should be pretty quick and efficient.
Calculations are still a wip.

Multiple tables can be created within the ANApy columnar data structure system.

.. code-block:: python

    import anapy.data_reader as dr
    import anapy.data_writer as dw
    from anapy.stash import StashTable


    def main():
        data = dr.DataReader(data='data.csv', format='csv').read()

        # stashing datasets to ANApy tables
        table = StashTable(data=data, table='basic_csv')
        table.save()

        # useful features for querying data
        col_names = table.col_names()
        first_row = table.row(index=0)
        first_col = table.col(key='email')

        # writing subsets of data to file
        females = table.get(key='gender', value='Female', operator='==')
        dw.write_csv(data=females, file='female_subset.csv')

        # removing tables once complete
        table.un_stash()


    if __name__ == '__main__':
        main()
