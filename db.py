''' Database related functions '''

import mysql.connector
from mysql.connector import errorcode
import sql.tables

# Hardcoded DB credentials, in production use Vault or some other service
DB_USER = "root"
DB_PASSWORD="@Py1234@"

def __init_db():
    ''' Create the storage database '''
    mydb = mysql.connector.connect(
        host="mysqldb",
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = mydb.cursor()

    cursor.execute("DROP DATABASE IF EXISTS storage")
    cursor.execute("CREATE DATABASE storage")
    cursor.close()

def __init_tables():
    ''' Create the default tables '''
    mydb = mysql.connector.connect(
        host="mysqldb",
        user=DB_USER,
        password=DB_PASSWORD,
        database="storage"
    )
    cursor = mydb.cursor()
    for key, value in sql.tables.TABLES.items():
        try:
            print(f"Creating table {key}: ", end='')
            cursor.execute(value)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")
    cursor.close()

def init():
    ''' Initilization function for the DB '''
    __init_db()
    __init_tables()
