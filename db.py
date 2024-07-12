# pip install pymysql
# pip freeze > requirements.txt

import pymysql

host = "localhost"
user = "root"
password = ""
db = "wawdb"

#Datos para Pythonanywhere:

# host = "holaclaris.mysql.pythonanywhere-services.com"
# user = "holaclaris"
# password = "lunita29"
# db = "holaclaris$waw"

def conexionMySQL():
    return pymysql.connect(host=host, user=user, password=password, database=db)
