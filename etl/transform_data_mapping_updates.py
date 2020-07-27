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

#  1. cap-shape: bell=b,conical=c,convex=x,flat=f, knobbed=k,sunken=s
#  cap-shape changes
    try:
        print("'{}' [cap-shape] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [cap-shape] = 'bell' WHERE [cap-shape] = 'b'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' cap-shape mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, cap-shape changes not applied')

#  cap-shape changes
    try:
        print("'{}' [cap-shape] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [cap-shape] = 'conical' WHERE [cap-shape] = 'c'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' cap-shape mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, cap-shape changes not applied')

#  cap-shape changes
    try:
        print("'{}' [cap-shape] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [cap-shape] = 'convex' WHERE [cap-shape] = 'x'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' cap-shape mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, cap-shape changes not applied')

#  cap-shape changes
    try:
        print("'{}' [cap-shape] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [cap-shape] = 'flat' WHERE [cap-shape] = 'f'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' cap-shape mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, cap-shape changes not applied')

#  cap-shape changes
    try:
        print("'{}' [cap-shape] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [cap-shape] = 'knobbed' WHERE [cap-shape] = 'k'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' cap-shape mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, cap-shape changes not applied')

#  cap-shape changes
    try:
        print("'{}' [cap-shape] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [cap-shape] = 'sunken' WHERE [cap-shape] = 's'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' cap-shape mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, cap-shape changes not applied')


# cap-color: brown=n,buff=b,cinnamon=c,gray=g,green=r, pink=p,purple=u,red=e,white=w,yellow=y
#  cap-color changes
    try:
        print("'{}' [cap-color] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [cap-color] = 'brown' WHERE [cap-color] = 'n'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' cap-color mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, cap-color changes not applied')

#  cap-color changes
    try:
        print("'{}' [cap-color] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [cap-color] = 'cinnamon' WHERE [cap-color] = 'c'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' cap-color mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, cap-color changes not applied')

#  cap-color changes
    try:
        print("'{}' [cap-color] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [cap-color] = 'gray' WHERE [cap-color] = 'g'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' cap-color mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, cap-color changes not applied')

#  cap-color changes
    try:
        print("'{}' [cap-color] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [cap-color] = 'green' WHERE [cap-color] = 'g'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' cap-color mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, cap-color changes not applied')

#  cap-color changes
    try:
        print("'{}' [cap-color] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [cap-color] = 'pink' WHERE [cap-color] = 'p'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' cap-color mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, cap-color changes not applied')

#  cap-color changes
    try:
        print("'{}' [cap-color] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [cap-color] = 'purple' WHERE [cap-color] = 'u'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' cap-color mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, cap-color changes not applied')

#  cap-color changes
    try:
        print("'{}' [cap-color] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [cap-color] = 'red' WHERE [cap-color] = 'e'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' cap-color mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, cap-color changes not applied')

#  cap-color changes
    try:
        print("'{}' [cap-color] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [cap-color] = 'white' WHERE [cap-color] = 'w'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' cap-color mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, cap-color changes not applied')


#  cap-color changes
    try:
        print("'{}' [cap-color] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [cap-color] = 'yellow' WHERE [cap-color] = 'y'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' cap-color mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, cap-color changes not applied')


# odor: almond=a,anise=l,creosote=c,fishy=y,foul=f, musty=m,none=n,pungent=p,spicy=s
#  odor changes
    try:
        print("'{}' [odor] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [odor] = 'almond' WHERE [odor] = 'a'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' odor mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, odor changes not applied')

#  odor changes
    try:
        print("'{}' [odor] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [odor] = 'anise' WHERE [odor] = 'l'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' odor mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, odor changes not applied')

#  odor changes
    try:
        print("'{}' [odor] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [odor] = 'creosote' WHERE [odor] = 'c'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' odor mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, odor changes not applied')

#  odor changes
    try:
        print("'{}' [odor] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [odor] = 'fishy' WHERE [odor] = 'y'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' odor mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, odor changes not applied')

#  odor changes
    try:
        print("'{}' [odor] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [odor] = 'foul' WHERE [odor] = 'f'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' odor mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, odor changes not applied')

#  odor changes
    try:
        print("'{}' [odor] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [odor] = 'musty' WHERE [odor] = 'm'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' odor mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, odor changes not applied')

#  odor changes
    try:
        print("'{}' [odor] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [odor] = 'none' WHERE [odor] = 'n'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' odor mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, odor changes not applied')

#  odor changes
    try:
        print("'{}' [odor] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [odor] = 'pungent' WHERE [odor] = 'p'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' odor mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, odor changes not applied')


#  odor changes
    try:
        print("'{}' [odor] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [odor] = 'spicy' WHERE [odor] = 's'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' odor mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, odor changes not applied')


# gill-size: broad=b,narrow=n
#  gill-size changes
    try:
        print("'{}' [gill-size] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [gill-size] = 'broad' WHERE [gill-size] = 'b'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' gill-size mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, gill-size changes not applied')

#  gill-size changes
    try:
        print("'{}' [gill-size] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [gill-size] = 'narrow' WHERE [gill-size] = 'n'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' gill-size mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, gill-size changes not applied')


# gill-color: black=k,brown=n,buff=b,chocolate=h,gray=g, green=r,orange=o,pink=p,purple=u,red=e, white=w,yellow=y
#  gill-color changes
    try:
        print("'{}' [gill-color] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [gill-color] = 'black' WHERE [gill-color] = 'k'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' gill-color mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, gill-color changes not applied')

#  gill-color changes
    try:
        print("'{}' [gill-color] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [gill-color] = 'brown' WHERE [gill-color] = 'n'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' gill-color mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, gill-color changes not applied')

#  gill-color changes
    try:
        print("'{}' [gill-color] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [gill-color] = 'buff' WHERE [gill-color] = 'b'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' gill-color mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, gill-color changes not applied')

#  gill-color changes
    try:
        print("'{}' [gill-color] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [gill-color] = 'chocolate' WHERE [gill-color] = 'h'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' gill-color mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, gill-color changes not applied')

#  gill-color changes
    try:
        print("'{}' [gill-color] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [gill-color] = 'gray' WHERE [gill-color] = 'g'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' gill-color mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, gill-color changes not applied')

#  gill-color changes
    try:
        print("'{}' [gill-color] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [gill-color] = 'green' WHERE [gill-color] = 'r'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' gill-color mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, gill-color changes not applied')

#  gill-color changes
    try:
        print("'{}' [gill-color] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [gill-color] = 'orange' WHERE [gill-color] = 'o'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' gill-color mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, gill-color changes not applied')

#  gill-color changes
    try:
        print("'{}' [gill-color] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [gill-color] = 'pink' WHERE [gill-color] = 'p'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' gill-color mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, gill-color changes not applied')


#  gill-color changes
    try:
        print("'{}' [gill-color] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [gill-color] = 'purple' WHERE [gill-color] = 'u'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' gill-color mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, gill-color changes not applied')

#  gill-color changes
    try:
        print("'{}' [gill-color] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [gill-color] = 'red' WHERE [gill-color] = 'e'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' gill-color mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, gill-color changes not applied')


#  gill-color changes
    try:
        print("'{}' [gill-color] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [gill-color] = 'white' WHERE [gill-color] = 'w'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' gill-color mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, gill-color changes not applied')


#  gill-color changes
    try:
        print("'{}' [gill-color] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [gill-color] = 'yellow' WHERE [gill-color] = 'y'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' gill-color mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, gill-color changes not applied')


# stalk-color-above-ring: brown=n,buff=b,cinnamon=c,gray=g,orange=o, pink=p,red=e,white=w,yellow=y
#  stalk-color-above-ring changes
    try:
        print(
            "'{}' [stalk-color-above-ring] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [stalk-color-above-ring] = 'brown' WHERE [stalk-color-above-ring] = 'n'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' stalk-color-above-ring mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, stalk-color-above-ring changes not applied')

#  stalk-color-above-ring changes
    try:
        print(
            "'{}' [stalk-color-above-ring] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [stalk-color-above-ring] = 'buff' WHERE [stalk-color-above-ring] = 'b'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' stalk-color-above-ring mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, stalk-color-above-ring changes not applied')

#  stalk-color-above-ring changes
    try:
        print(
            "'{}' [stalk-color-above-ring] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [stalk-color-above-ring] = 'cinnamon' WHERE [stalk-color-above-ring] = 'c'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' stalk-color-above-ring mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, stalk-color-above-ring changes not applied')

#  stalk-color-above-ring changes
    try:
        print(
            "'{}' [stalk-color-above-ring] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [stalk-color-above-ring] = 'gray' WHERE [stalk-color-above-ring] = 'g'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' stalk-color-above-ring mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, stalk-color-above-ring changes not applied')

#  stalk-color-above-ring changes
    try:
        print(
            "'{}' [stalk-color-above-ring] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [stalk-color-above-ring] = 'orange' WHERE [stalk-color-above-ring] = 'o'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' stalk-color-above-ring mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, stalk-color-above-ring changes not applied')

#  stalk-color-above-ring changes
    try:
        print(
            "'{}' [stalk-color-above-ring] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [stalk-color-above-ring] = 'pink' WHERE [stalk-color-above-ring] = 'p'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' stalk-color-above-ring mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, stalk-color-above-ring changes not applied')

#  stalk-color-above-ring changes
    try:
        print(
            "'{}' [stalk-color-above-ring] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [stalk-color-above-ring] = 'red' WHERE [stalk-color-above-ring] = 'e'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' stalk-color-above-ring mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, stalk-color-above-ring changes not applied')

#  stalk-color-above-ring changes
    try:
        print(
            "'{}' [stalk-color-above-ring] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [stalk-color-above-ring] = 'white' WHERE [stalk-color-above-ring] = 'w'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' stalk-color-above-ring mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, stalk-color-above-ring changes not applied')


#  stalk-color-above-ring changes
    try:
        print(
            "'{}' [stalk-color-above-ring] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [stalk-color-above-ring] = 'yellow' WHERE [stalk-color-above-ring] = 'y'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' stalk-color-above-ring mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, stalk-color-above-ring changes not applied')


# veil-color: brown=n,orange=o,white=w,yellow=y
#  veil-color changes
    try:
        print("'{}' [veil-color] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [veil-color] = 'brown' WHERE [veil-color] = 'n'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' veil-color mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, veil-color changes not applied')

#  veil-color changes
    try:
        print("'{}' [veil-color] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [veil-color] = 'orange' WHERE [veil-color] = 'o'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' veil-color mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, veil-color changes not applied')

#  veil-color changes
    try:
        print("'{}' [veil-color] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [veil-color] = 'white' WHERE [veil-color] = 'w'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' veil-color mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, veil-color changes not applied')

#  veil-color changes
    try:
        print("'{}' [veil-color] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [veil-color] = 'yellow' WHERE [veil-color] = 'y'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' veil-color mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, veil-color changes not applied')


# ring-type: cobwebby=c,evanescent=e,flaring=f,large=l, none=n,pendant=p,sheathing=s,zone=z
#  ring-type changes
    try:
        print("'{}' [ring-type] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [ring-type] = 'cobwebby' WHERE [ring-type] = 'c'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' ring-type mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, ring-type changes not applied')

#  ring-type changes
    try:
        print("'{}' [ring-type] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [ring-type] = 'evanescent' WHERE [ring-type] = 'e'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' ring-type mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, ring-type changes not applied')

#  ring-type changes
    try:
        print("'{}' [ring-type] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [ring-type] = 'flaring' WHERE [ring-type] = 'f'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' ring-type mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, ring-type changes not applied')

#  ring-type changes
    try:
        print("'{}' [ring-type] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [ring-type] = 'large' WHERE [ring-type] = 'l'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' ring-type mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, ring-type changes not applied')

#  ring-type changes
    try:
        print("'{}' [ring-type] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [ring-type] = 'none' WHERE [ring-type] = 'n'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' ring-type mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, ring-type changes not applied')

#  ring-type changes
    try:
        print("'{}' [ring-type] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [ring-type] = 'pendant' WHERE [ring-type] = 'p'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' ring-type mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, ring-type changes not applied')

#  ring-type changes
    try:
        print("'{}' [ring-type] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [ring-type] = 'sheathing' WHERE [ring-type] = 's'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' ring-type mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, ring-type changes not applied')

#  ring-type changes
    try:
        print("'{}' [ring-type] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [ring-type] = 'zone' WHERE [ring-type] = 'z'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' ring-type mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, ring-type changes not applied')


# spore-print-color: black=k,brown=n,buff=b,chocolate=h,green=r, orange=o,purple=u,white=w,yellow=y
#  spore-print-color changes
    try:
        print(
            "'{}' [spore-print-color] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [spore-print-color] = 'black' WHERE [spore-print-color] = 'k'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' spore-print-color mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, spore-print-color changes not applied')

#  spore-print-color changes
    try:
        print(
            "'{}' [spore-print-color] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [spore-print-color] = 'brown' WHERE [spore-print-color] = 'n'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' spore-print-color mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, spore-print-color changes not applied')

#  spore-print-color changes
    try:
        print(
            "'{}' [spore-print-color] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [spore-print-color] = 'buff' WHERE [spore-print-color] = 'b'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' spore-print-color mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, spore-print-color changes not applied')

#  spore-print-color changes
    try:
        print(
            "'{}' [spore-print-color] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [spore-print-color] = 'chocolate' WHERE [spore-print-color] = 'h'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' spore-print-color mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, spore-print-color changes not applied')

#  spore-print-color changes
    try:
        print(
            "'{}' [spore-print-color] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [spore-print-color] = 'green' WHERE [spore-print-color] = 'r'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' spore-print-color mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, spore-print-color changes not applied')

#  spore-print-color changes
    try:
        print(
            "'{}' [spore-print-color] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [spore-print-color] = 'orange' WHERE [spore-print-color] = 'o'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' spore-print-color mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, spore-print-color changes not applied')

#  spore-print-color changes
    try:
        print(
            "'{}' [spore-print-color] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [spore-print-color] = 'purple' WHERE [spore-print-color] = 'u'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' spore-print-color mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, spore-print-color changes not applied')

#  spore-print-color changes
    try:
        print(
            "'{}' [spore-print-color] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [spore-print-color] = 'white' WHERE [spore-print-color] = 'w'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' spore-print-color mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, spore-print-color changes not applied')


#  spore-print-color changes
    try:
        print(
            "'{}' [spore-print-color] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [spore-print-color] = 'yellow' WHERE [spore-print-color] = 'y'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' spore-print-color mappings updated.".format(table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, spore-print-color changes not applied')


# population: abundant=a,clustered=c,numerous=n, scattered=s,several=v,solitary=y
#  population changes
    try:
        print("'{}' [population] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [population] = 'abundant' WHERE [population] = 'a'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' population mappings updated.".format(
            table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, population changes not applied')

#  population changes
    try:
        print("'{}' [population] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [population] = 'clustered' WHERE [population] = 'c'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' population mappings updated.".format(
            table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, population changes not applied')

#  population changes
    try:
        print("'{}' [population] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [population] = 'numerous' WHERE [population] = 'n'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' population mappings updated.".format(
            table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, population changes not applied')

#  population changes
    try:
        print("'{}' [population] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [population] = 'scattered' WHERE [population] = 's'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' population mappings updated.".format(
            table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, population changes not applied')

#  population changes
    try:
        print("'{}' [population] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [population] = 'several' WHERE [population] = 'v'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' population mappings updated.".format(
            table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, population changes not applied')

#  population changes
    try:
        print("'{}' [population] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [population] = 'solitary' WHERE [population] = 'y'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' population mappings updated.".format(
            table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, population changes not applied')


# habitat: grasses=g,leaves=l,meadows=m,paths=p, urban=u,waste=w,woods=d
#  habitat changes
    try:
        print("'{}' [habitat] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [habitat] = 'grasses' WHERE [habitat] = 'g'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' habitat mappings updated.".format(
            table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, habitat changes not applied')

#  habitat changes
    try:
        print("'{}' [habitat] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [habitat] = 'leaves' WHERE [habitat] = 'l'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' habitat mappings updated.".format(
            table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, habitat changes not applied')

#  habitat changes
    try:
        print("'{}' [habitat] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [habitat] = 'meadows' WHERE [habitat] = 'm'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' habitat mappings updated.".format(
            table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, habitat changes not applied')

#  habitat changes
    try:
        print("'{}' [habitat] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [habitat] = 'paths' WHERE [habitat] = 'p'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' habitat mappings updated.".format(
            table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, habitat changes not applied')

#  habitat changes
    try:
        print("'{}' [habitat] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [habitat] = 'urban' WHERE [habitat] = 'u'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' habitat mappings updated.".format(
            table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, habitat changes not applied')

#  habitat changes
    try:
        print("'{}' [habitat] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [habitat] = 'waste' WHERE [habitat] = 'w'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' habitat mappings updated.".format(
            table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, habitat changes not applied')

#  habitat changes
    try:
        print("'{}' [habitat] mapping updates.".format(table_staging_clean))
        sql_query = "UPDATE [dbo].[specimen_clean] SET  [habitat] = 'woods' WHERE [habitat] = 'd'; "

    # print(sql_query)

        cur.execute(sql_query)
        print("staging table '{}' habitat mappings updated.".format(
            table_staging_clean))
        #print("query ran successfully ")
    # connection.Commit()
    except:
        print('Connection failed to SQL Server, habitat changes not applied')


# if staging table is empty
if row_count == 0:
    print("staging table clean '{}' is empty, table not loaded properly, no action will be taken (extract_load_data must be executed berfore running this script)".format(
        table_staging_clean))

# After all operation is done close the database connection
connection.close()
print('connection closed')
