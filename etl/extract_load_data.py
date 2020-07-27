"""
Author: Collins Emetonjor       Date: 24/07/2020     Comment: script to create 'sh_dev' db on a target SQL server
                                                              Details for DB name, server, username & password are in the variable.py file

Change History
Author:                         Date:                Comment

"""
# import ODBC Python module
import pyodbc

# import variables
from variable import server, username, password, database_name, table_staging_raw, table_staging_clean, path_to_file


# check if database exist in the SQL Server

# Connecting to MS SQL Server
connection = None
try:
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                                server+';UID='+username+';PWD=' + password+';Database=' + database_name)

    print('Connected to SQL Server Successfully')
except:
    print('Connection failed to SQL Server')

if connection is not None:
    connection.autocommit = True

cur = connection.cursor()

# get count of records in staging table
sql_query = "SELECT count(1) FROM " + table_staging_raw

# print(sql_query)

# staging table row count
cur.execute(sql_query)

row_count = cur.fetchall()

# convert data from list to string in order to use the string replace method
row_count = (str(row_count[0]))

# applying the string replace method
row_count = row_count.replace(', )', '').replace('(', '')

# convert data to int
row_count = int(row_count)

# print(data)

# checking what type of loading is needed

# if staging table already contains data, then do a truncate before loading data
if row_count > 0:
 # create staging table
    print("staging tables '{}, {}' have data, tables will be truncated.".format(
        table_staging_raw, table_staging_clean))

    try:
        print("truncating table '{}'.".format(table_staging_raw))
        sql_query = "TRUNCATE TABLE {}".format(table_staging_raw)

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' truncated.".format(table_staging_raw))

        sql_query = "BULK INSERT " + table_staging_raw + " FROM " + \
            path_to_file + " WITH ( FORMAT='CSV', FIRSTROW=2)"
        print("running query: " + sql_query)
        cur.execute(sql_query)
        print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server')

    try:
        print("truncating table '{}'.".format(table_staging_clean))
        sql_query = "TRUNCATE TABLE {}".format(table_staging_clean)

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' truncated.".format(table_staging_clean))

        sql_query = "BULK INSERT " + table_staging_clean + " FROM " + \
            path_to_file + " WITH ( FORMAT='CSV', FIRSTROW=2)"
        print("running query: " + sql_query)
        cur.execute(sql_query)
        print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server')


# if staging table is empty, then load data immediately
if row_count == 0:
    print("staging tables '{}, {}' are empty, data will be loaded now.".format(
        table_staging_raw, table_staging_clean))

    print("loading table '{}'.".format(table_staging_raw))
    try:
        sql_query = "BULK INSERT " + table_staging_raw + " FROM " + \
            path_to_file + " WITH ( FORMAT='CSV', FIRSTROW=2)"
        print("running query: " + sql_query)

        cur.execute(sql_query)
        print("query ran successfully ")
    except:
        print('Connection failed to SQL Server')

    print("loading table '{}'.".format(table_staging_clean))
    try:
        sql_query = "BULK INSERT " + table_staging_clean + " FROM " + \
            path_to_file + " WITH ( FORMAT='CSV', FIRSTROW=2)"
        print("running query: " + sql_query)

        cur.execute(sql_query)
        print("query ran successfully ")

    except:
        print('Connection failed to SQL Server')

# After all operation is done close the database connection
connection.close()
print('connection closed')
