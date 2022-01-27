import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ssp"
)
cursor = mydb.cursor()

# createTableQuery = "CREATE TABLE users(id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR (50) UNIQUE, " \
#                    "originalPass VARCHAR(50), pass1 VARCHAR(50), " \
#                    "pass2 VARCHAR(50), pass3 VARCHAR(50), pass4 VARCHAR(50), pass5 VARCHAR(50), pass6 VARCHAR(50), " \
#                    "pass7 VARCHAR(50), pass8 VARCHAR(50), pass9 VARCHAR(50), pass10 VARCHAR(50), pass11 VARCHAR(50), " \
#                    "pass12 VARCHAR(50), pass13 VARCHAR(50), pass14 VARCHAR(50), pass15 VARCHAR(50), pass16 VARCHAR(50), " \
#                    "pass17 VARCHAR(50), pass18 VARCHAR(50), pass19 VARCHAR(50), pass20 VARCHAR(50), pass21 VARCHAR(50), " \
#                    "pass22 VARCHAR(50), pass23 VARCHAR(50), pass24 VARCHAR(50))"
#
# cursor.execute(createTableQuery)
