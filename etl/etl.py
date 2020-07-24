import urllib.request

print('Beginning file download with urllib2...')

url = 'https://github.com/collins-emetonjor/sh_etl_projects/blob/master/data/sh_data.csv'
urllib.request.urlretrieve(url, 'cat1.csv')

"""
import urllib.request
url = 'https://github.com/collins-emetonjor/sh_etl_projects/blob/master/data/Senior%20Data%20Engn-%20agaricus-lepiota%20-%20send.csv'
print("download start!")
filename, headers = urllib.request.urlretrieve(
    url, filename="nron_mail_20150507.tgz")
print("download complete!")
print("download file location: ", filename)
print("download headers: ", headers)


# Import packages
import pandas as pd
# Assign url of file: url
url = 'https://github.com/collins-emetonjor/sh_etl_projects/blob/master/data/Senior%20Data%20Engn-%20agaricus-lepiota%20-%20send.csv'
# Read file into a DataFrame: df
df = pd.read_csv(url, sep='\t', error_bad_lines=False)
# Print the head of the DataFrame
#df = lg.read_csv("my.csv")
print(df.head())


df.head(5)
"""
