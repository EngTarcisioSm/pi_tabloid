# pode haver algum erro aqui

# import mysql.connector

# mydb = mysql.connector.connect(
#     host= "localhost",
#     user="root",
#     passwd="123",

# )
# my_cursor = mydb.cursor()

# my_cursor.execute("CREATE DATABASE tabloid")

# my_cursor.execute("SHOW DATABASES")

# for db in my_cursor:
#     print(db)

import psycopg2

mydb = psycopg2.connect(
    host= "localhost",
    user="root",
    passwd="123",

)
my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE tabloid")

my_cursor.execute("SHOW DATABASES")

for db in my_cursor:
    print(db)