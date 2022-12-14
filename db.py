# import pyodbc
# server = 'schoolnetdb.database.windows.net'
# database = 'SchoolNETDataBase'
# username = 'schoolnetadmin'
# password = 'schoolnetpass000!'
# driver= '{ODBC Driver 17 for SQL Server}'

# with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
#     with conn.cursor() as cursor:
#         cursor.execute("SELECT * FROM dbo.C_Team_Admin")
#         row = cursor.fetchone()
#         while row:
#             print (str(row[0]) + " " + str(row[1]))
#             row = cursor.fetchone()


import mysql.connector

# データベースに接続

connection = mysql.connector.connect(host='schoolnetdb.database.windows.net',

                                    user='schoolnetadmin',

                                    port='1443',

                                    password='schoolnetpass000!',

                                    database='SchoolNETDataBase')



with connection.cursor() as cursor:

        # データ読み込み

        sql = "SELECT * FROM dbo.C_Team_Admin"

        cursor.execute(sql)

        result = cursor.fetchall()

        print(result)



# 終了処理

cursor.close()
