import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="localhost",
  password="localhost"
)

print(mydb)