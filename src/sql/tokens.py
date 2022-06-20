''' Module for managing tokens with the DB '''
ADD_TOKEN = "INSERT INTO tokens (token, role) VALUES (%s, %s)"
GET_TOKEN = "SELECT role FROM tokens WHERE token = %s"
