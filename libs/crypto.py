''' Module for cryptographic functions '''
import hashlib

def hash_password(password):
    ''' Generate SHA512 hash from given password, in readable format '''
    return hashlib.sha512(str(password).encode("utf-8")).hexdigest()
