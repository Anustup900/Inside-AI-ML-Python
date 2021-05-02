import mysql.connector 


insideAIMLdb = mysql.connector.connect(
host = "localhost",
user ="localhost",
password = "localhost"
)

print(insideAIMLdb)