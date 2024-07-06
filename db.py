# pip install pymysql
# pip freeze > requirements.txt

import pymysql

host = "localhost"
user = "root"
password = ""
db = "wawdb"

def conexionMySQL():
    return pymysql.connect(host=host, user=user, password=password, database=db)