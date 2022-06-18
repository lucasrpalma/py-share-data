import mysql.connector
from mysql.connector import errorcode
import sql.tables

# Hardcoded DB credentials, in production use Vault or some other service
db_user = "root"
db_password="@Py1234@"

def create_database():
    mydb = mysql.connector.connect(
        host="mysqldb",
        user=db_user,
        password=db_password
    )
    cursor = mydb.cursor()

    cursor.execute("DROP DATABASE IF EXISTS storage")
    cursor.execute("CREATE DATABASE storage")
    cursor.close()

def create_tables():
    mydb = mysql.connector.connect(
        host="mysqldb",
        user=db_user,
        password=db_password,
        database="storage"
    )
    cursor = mydb.cursor()
    for table_name in sql.tables.TABLES:
        table_description = sql.tables.TABLES[table_name]
        try:
            print("Creating table {}: ".format(table_name), end='')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")
    cursor.close()

def init():
    create_database()
    create_tables()