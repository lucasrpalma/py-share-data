''' Module for managing users with the DB '''
import sys
sys.path.append('../libs')
from libs import crypto

# Roles
ROLES = {}
ROLES['ADMIN'] = "superuser"
ROLES['PRIVACY'] = "privacy"
ROLES['FINANCE'] = "finance"
ROLES['REGULAR'] = "common"

# Users
USERS = {}
USERS['ADMIN'] = (1, 'admin', ROLES['ADMIN'], crypto.hash_password('1' + 'admin123' + '1'))
USERS['PRIVACY'] = (2, 'dpo', ROLES['PRIVACY'], crypto.hash_password('2' + 'dpo123' + '2'))
USERS['FINANCE'] = (3, 'payment', ROLES['FINANCE'], crypto.hash_password('3' + 'payment123' + '3'))
USERS['REGULAR'] = (4, 'user', ROLES['REGULAR'], crypto.hash_password('4' + 'user123' + '4'))

# Queries
ADD_USER = "INSERT INTO users (ID, username, role, password) VALUES (%s, %s, %s, %s)"
GET_USER_ID = "SELECT ID FROM users WHERE username = %s"
GET_USER_ROLE = "SELECT role FROM users WHERE id = %s AND password = %s"
