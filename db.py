''' Database related functions '''
import mysql.connector
from mysql.connector import errorcode
import sql.tables
import sql.users

# Hardcoded DB credentials, in production use Vault or some other service
DB_USER = "root"
DB_PASSWORD="@Py1234@"
DB_HOST = "mysqldb"
DB_NAME = "storage"

def __init_db():
    ''' Create the storage database '''
    mydb = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = mydb.cursor()

    cursor.execute("DROP DATABASE IF EXISTS storage")
    cursor.execute("CREATE DATABASE storage")
    cursor.close()
    mydb.close()

def __init_tables():
    ''' Create the default tables '''
    mydb = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
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
    mydb.close()

def __init_users():
    ''' Create the default users '''
    mydb = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = mydb.cursor()
    for key, value in sql.users.USERS.items():
        try:
            print(f"Inserting user {key}: ", end='')
            cursor.execute(sql.users.ADD_USER, value)
        except mysql.connector.Error as err:
            print('Error: ' + err.msg)
        else:
            print("OK")
    mydb.commit()
    cursor.close()
    mydb.close()

def init():
    ''' Initilization function for the DB '''
    __init_db()
    __init_tables()
    __init_users()

def get_user_id(username):
    ''' Query to get the id from a given username '''
    mydb = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = mydb.cursor()
    try:
        print(f"Querying user {username} ID: ", end='')
        cursor.execute(sql.users.GET_USER_ID, (username,))
        result = cursor.fetchone()
        user_id = None
        if result is None:
            print('Error: Username doesn\'t exist.')
        else:
            user_id = result[0]
    except mysql.connector.Error as err:
        print('Error: ' + err.msg)
    else:
        print(user_id)
        cursor.close()
        mydb.close()
        return user_id

def get_user_role(id, password):
    ''' Query to get the role from a given user ID, if the password is correct '''
    mydb = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = mydb.cursor()
    role = None
    try:
        print(f"Querying role from user [ID {id}]: ", end='')
        cursor.execute(sql.users.GET_USER_ROLE, (id, password))
        result = cursor.fetchone()
        if result is None:
            print('Error: Wrong password.')
        else:
            role = result[0]
            print(role)
        cursor.close()
        mydb.close()
    except mysql.connector.Error as err:
        print('Error: ' + err.msg)
    return role
