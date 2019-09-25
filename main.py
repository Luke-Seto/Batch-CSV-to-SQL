import bcpy
import pyodbc
from os import listdir
from os.path import isfile, join
# Connection to database
conn = pyodbc.connect("DRIVER={{SQL Server Native Client 11.0}}; SERVER=DISENGSQLPR1; DATABASE=Fis_Coned; UID={0}; PWD={1};".format('netstorm_ro', 'netstorm_ro'))
cursor = conn.cursor()
#Name for table
sql_table_name = input("Table Name ")
#Deletes data in table
query = """DELETE FROM FIS_CONED.dbo."""+sql_table_name
cursor.execute(query)
cursor.close()
conn.commit()
conn.close()
print('Deleted Data')

#connection to bcpy
sql_config = {
    'server': 'DISENGSQLPR1',
    'database': 'Fis_Coned',
    'username': 'netstorm_ro',
    'password': 'netstorm_ro'
}
#path the folder where csv file is
dirName = "C:\\Users\\setol\\Desktop\\upload csv"
#List all files from path
fileNames = [f for f in listdir(dirName) if isfile(join(dirName, f))]
x = (len(fileNames))

i = 0

while i < x:
  print(str(i)+'. '+fileNames[i])
  i += 1

#Enter file number
num = int(input("Enter Number of CSV File "))
print(fileNames[num])
#Uploades csv to database
csv_file_path = fileNames[num]
flat_file = bcpy.FlatFile(qualifier='', path=csv_file_path)
sql_table = bcpy.SqlTable(sql_config, table=sql_table_name)
flat_file.to_sql(sql_table)
print('Done')

