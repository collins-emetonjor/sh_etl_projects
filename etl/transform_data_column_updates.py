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

sql_query = "SELECT count(1) FROM " + table_staging_clean

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
    print("staging table (clean) '{}' has data, updates will be applied now.".format(
        table_staging_clean))

# renaming _1 column
    try:
        print("renaming '{}' table columns.".format(table_staging_clean))
        sql_query = "EXEC sp_rename '[dbo].[specimen_clean].[_1]', 'cap-shape', 'COLUMN';"

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' column (_1) updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, _1 column name changes not applied')

 # renaming _3 column
    try:
        print("renaming '{}' table columns.".format(table_staging_clean))
        sql_query = "EXEC sp_rename '[dbo].[specimen_clean].[_3]', 'cap-color', 'COLUMN';"

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' column (_3) updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, _3 column name changes not applied')

 # renaming _5 column
    try:
        print("renaming '{}' table columns.".format(table_staging_clean))
        sql_query = "EXEC sp_rename '[dbo].[specimen_clean].[_5]', 'odor', 'COLUMN';"

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' column (_5) updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, _5 column name changes not applied')

 # renaming _8 column
    try:
        print("renaming '{}' table columns.".format(table_staging_clean))
        sql_query = "EXEC sp_rename '[dbo].[specimen_clean].[_8]', 'gill-size', 'COLUMN';"

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' column (_8) updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, _8 column name changes not applied')

 # renaming _9 column
    try:
        print("renaming '{}' table columns.".format(table_staging_clean))
        sql_query = "EXEC sp_rename '[dbo].[specimen_clean].[_9]', 'gill-color', 'COLUMN';"

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' column (_9) updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, _9 column name changes not applied')

 # renaming _14 column
    try:
        print("renaming '{}' table columns.".format(table_staging_clean))
        sql_query = "EXEC sp_rename '[dbo].[specimen_clean].[_14]', 'stalk-color-above-ring', 'COLUMN';"

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' column (_14) updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, _14 column name changes not applied')

 # renaming _17 column
    try:
        print("renaming '{}' table columns.".format(table_staging_clean))
        sql_query = "EXEC sp_rename '[dbo].[specimen_clean].[_17]', 'veil-color', 'COLUMN';"

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' column (_17) updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, _17 column name changes not applied')

 # renaming _19 column
    try:
        print("renaming '{}' table columns.".format(table_staging_clean))
        sql_query = "EXEC sp_rename '[dbo].[specimen_clean].[_19]', 'ring-type', 'COLUMN';"

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' column (_19) updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, _19 column name changes not applied')

 # renaming _20 column
    try:
        print("renaming '{}' table columns.".format(table_staging_clean))
        sql_query = "EXEC sp_rename '[dbo].[specimen_clean].[_20]', 'spore-print-color', 'COLUMN';"

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' column (_20) updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, _20 column name changes not applied')

 # renaming _21 column
    try:
        print("renaming '{}' table columns.".format(table_staging_clean))
        sql_query = "EXEC sp_rename '[dbo].[specimen_clean].[_21]', 'population', 'COLUMN';"

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' column (_21) updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, _21 column name changes not applied')

 # renaming _22 column
    try:
        print("renaming '{}' table columns.".format(table_staging_clean))
        sql_query = "EXEC sp_rename '[dbo].[specimen_clean].[_22]', 'habitat', 'COLUMN';"

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' column (_22) updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, _22 column name changes not applied')


# if staging table is empty
if row_count == 0:
    print("staging table clean '{}' is empty, table not loaded properly, no action will be taken (extract_load_data must be executed berfore running this script)".format(
        table_staging_clean))

# After all operation is done close the database connection
connection.close()
print('connection closed')
