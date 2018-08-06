import pyodbc

from murkosha import murkosha_cats_list
from izpriuta import izpriuta_cats_list
from cat import Cat

server = 'cats-server.database.windows.net'
database = 'cats'
username = 'juliavav'
password = '********'
driver = '{ODBC Driver 13 for SQL Server}'

cnxn = pyodbc.connect(
    'DRIVER=' + driver + ';SERVER=' + server + ';PORT=1443;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
cursor = cnxn.cursor()
id_c = 4
cats = murkosha_cats_list()
cats.extend(izpriuta_cats_list())

for cat in cats:
    cursor.execute(
        "INSERT dbo.Cat_Info(NAME, AGE, SEX, IMAGE_URL) OUTPUT INSERTED.ID VALUES (N'{0}',N'{1}',N'{2}',N'{3}')".format(
            cat.name,
            cat.age,
            cat.sex,
            cat.img_url))
    print(cat.name)
    cnxn.commit()
    #row = cursor.fetchone()
    ++id_c
