# sh_etl_projects

This project was developed in python (3.8.3) and has three requested folders and an additional data folder which contains the mushroom dataset (flat file). 

A local SQL Server (2017) was used as the relational database management system.  

Within the python terminal, please install the following modules/packages
•	Pyodbc (pip install pyodbc) 	for SQL connectivity
•	Pandas (pip install pandas) 	for data analysis
•	Haversine (pip install haversine) for geographical calculations

Within the variables files (variable.py) in the db, etl, sql folders, please update the following variables

server = 'DESKTOP-U426G1T'

database_name = 'sh_staging'

username = 'sa'

password = 'ADMin12!@'

table_staging_raw = 'specimen_raw'

table_staging_clean = 'specimen_clean'

path_to_file = "'C:\Github\sh_etl_projects\data\sh_data.csv'"


**Folder List**
db: contains three files

1.	create_db.py: script to create the sql server DB

2.	create_table.py script to create the sql server staging tables

3.	variables: variables used by the python script

**etl: contains four files**
1.	extract_load_data.py: script to load the data from the flat file into the SQL staging tables

2.	transform_data_column_updates.py: script to update the columns of the staging tables. 

3.	transform_data_mapping_updates.py: script apply mappings. 

4.      variable.py

**sql: contains two files**

1.      sql.ipynb: This was implemented as a python notebook for clarity, please use a jupyter notebook or visual studio code notebook to open it. 

2.      variable.py

**Observations:**  I noticed that the mapping updates did not cater for every scenario e.g cap_shape field. No cleanup exercise was done on the data. 
 
