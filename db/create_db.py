"""
Author: Collins Emetonjor       Date: 24/07/2020     Comment: script to create 'sh_dev' db on a target SQL server
                                                              Details for DB name, server, username & password are in the variable.py file

Change History
Author:                         Date:                Comment

"""
# import ODBC Python module
import pyodbc

# import variables
from variable import server, username, password, database_name

# check if database exist in the SQL Server

# Connecting to MS SQL Server
connection = None
try:
    connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';UID='+username+';PWD=' + password)
    # connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+')
    print('Connected to SQL Server Successfully')
except:
    print('Connection failed to SQL Server')

if connection is not None:
    connection.autocommit = True

# converting database name to lower case for like for comparism
database_name = database_name.lower()

cur = connection.cursor()
cur.execute(
    "SELECT name FROM master.dbo.sysdatabases where LOWER(name)=?;", (database_name,))
data = cur.fetchall()

print(data)

# Printing if database exists or not
if not data:
    print("'{}' Database does not exist.".format(database_name))

 # create a new database db template (model db)
    print("Creating Database '{}'.".format(database_name))
    cur.execute("CREATE DATABASE {}".format(database_name))
    print("Database '{}' Created.".format(database_name))


else:
    print("'{}' Database already exists".format(database_name))

# After all operation is done close the database connection
connection.close()
print('connection closed')
