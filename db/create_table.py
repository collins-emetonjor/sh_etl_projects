"""
Author: Collins Emetonjor       Date: 24/07/2020     Comment: script to create staging tables

Change History
Author:                         Date:                Comment

"""
# import ODBC Python module
import pyodbc

# import variables
from variable import server, username, password, database_name, table_staging_raw, table_staging_clean

# convert table nanme to lower case
table_staging_raw = table_staging_raw.lower()

# print(table_staging_raw)


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

# checking if staging table (raw) exist
try:
    cur.execute("SELECT name FROM sys.tables where LOWER(name)=?;",
                (table_staging_raw,))
    table = cur.fetchall()

    print("staging table (raw) name: {}" .format(table))


# if staging table does not exist, then create it
    if not table:
        print("'{}' table does not exist.".format(table_staging_raw))

        sql_query = f'CREATE TABLE [dbo].[{table_staging_raw}] ( [_1] [nvarchar](100) NULL,[_3] [nvarchar](100) NULL,[_5] [nvarchar](100) NULL,[_8] [nvarchar](100) NULL,[_9] [nvarchar](100) NULL,[_14] [nvarchar](100) NULL,[_17] [nvarchar](100) NULL,[_19] [nvarchar](100) NULL,[_20] [nvarchar](100) NULL,[_21] [nvarchar](100) NULL,[_22] [nvarchar](100) NULL,[lat] [float]NULL,[lon] [float] NULL,[Time] [nvarchar](100) NULL) ON [PRIMARY]'

    #print (sql_query)

 # create staging table
        print("Creating table '{}'.".format(table_staging_raw))
        cur.execute(sql_query)
        print("table '{}' created Successfully.".format(table_staging_raw))

    else:
        print("'{}' table already exists".format(table_staging_raw))

except:
    print('staging table (raw) creation failed, check connection to sql server')


# checking if staging table (clean) exist
try:
    cur.execute("SELECT name FROM sys.tables where LOWER(name)=?;",
                (table_staging_clean,))
    table = cur.fetchall()

    print("staging table (clean) name: {}" .format(table))


# if staging table does not exist, then create it
    if not table:
        print("'{}' table does not exist.".format(table_staging_clean))

        sql_query = f'CREATE TABLE [dbo].[{table_staging_clean}] ( [_1] [nvarchar](100) NULL,[_3] [nvarchar](100) NULL,[_5] [nvarchar](100) NULL,[_8] [nvarchar](100) NULL,[_9] [nvarchar](100) NULL,[_14] [nvarchar](100) NULL,[_17] [nvarchar](100) NULL,[_19] [nvarchar](100) NULL,[_20] [nvarchar](100) NULL,[_21] [nvarchar](100) NULL,[_22] [nvarchar](100) NULL,[lat] [float]NULL,[lon] [float] NULL,[Time] [nvarchar](100) NULL) ON [PRIMARY]'

    #print (sql_query)

 # create staging table
        print("Creating table '{}'.".format(table_staging_clean))
        cur.execute(sql_query)
        print("table '{}' created Successfully.".format(table_staging_clean))

    else:
        print("'{}' table already exists".format(table_staging_clean))

except:
    print('staging table (clean) creation failed, check connection to sql server')

# After all operation is done close the database connection
connection.close()
print('connection closed')
