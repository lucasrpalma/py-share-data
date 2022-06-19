''' Module with the users needed for this exercise '''
import sys
sys.path.append('../libs')
from libs import crypto

USERS = {}
ADD_USER = "INSERT INTO users (ID, username, role, password) VALUES (%s, %s, %s, %s)"

USERS['ADMIN'] = (1,'admin','superuser', crypto.hash_password('1' + 'admin123' + '1'))
USERS['PRIVACY'] = (2,'dpo','privacy',crypto.hash_password('2' + 'dpo123' + '2'))
USERS['FINANCE'] = (3,'payment','finance',crypto.hash_password('3' + 'payment123' + '3'))
USERS['REGULAR'] = (4,'user','common',crypto.hash_password('4' + 'user123' + '4'))

GET_USER_ID = "SELECT ID FROM users WHERE username = %s"
GET_USER_ROLE = "SELECT role FROM users WHERE id = %s AND password = %s"
