import pyodbc
server = 'schoolnetdb.database.windows.net'
database = 'SchoolNETDataBase'
username = 'schoolnetadmin'
password = 'schoolnetpass000!'
driver= '{ODBC Driver 17 for SQL Server}'

with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM dbo.C_Team_Admin")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]))
            row = cursor.fetchone()
