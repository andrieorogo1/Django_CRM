# INSTALL Mysql on your computer 
# https://dev.mysql.com/downloads/installer/
# pip install mysql
# pip install mysql-connector
# pip intall mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'Cpk263491sdom$',

    )

# prepare cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE andrie")

print("All Done!")