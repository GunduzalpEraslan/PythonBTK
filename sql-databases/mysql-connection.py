# pip install mysql-connector

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost", #192.23.45.56 server adress olabilir
    user = "root",
    password = "123123",
    database = "mydatabase"
)

mycursor = mydb.cursor()

# mycursor.execute("SHOW DATABASES")
# mycursor.execute("CREATE DATABASE mydatabase")
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), adress VARCHAR(50))")

for x in mycursor:
    print(x)

print(mydb)