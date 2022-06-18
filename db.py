import mysql.connector

# Hardcoded DB credentials, in production use Vault or some other service
db_user = "root"
db_password="@Py1234@"

def init():
    mydb = mysql.connector.connect(
        host="mysqldb",
        user=db_user,
        password=db_password
    )
    cursor = mydb.cursor()

    cursor.execute("DROP DATABASE IF EXISTS storage")
    cursor.execute("CREATE DATABASE storage")
    cursor.close()

    mydb = mysql.connector.connect(
        host="mysqldb",
        user=db_user,
        password=db_password,
        database="storage"
    )
    cursor = mydb.cursor()
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute("CREATE TABLE users (id INT, login VARCHAR(255), role VARCHAR(255), password VARCHAR(255))")
    cursor.close()