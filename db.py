# pip install pymysql
# pip freeze > requirements.txt

import pymysql

host = "SofiaBaldera369.mysql.pythonanywhere-services.com"
user = "SofiaBaldera369"
password = "wawviajes"
db = "SofiaBaldera369$predeterminado"

def conexionMySQL():
    return pymysql.connect(host=host, user=user, password=password, database=db)
