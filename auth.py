''' Some authentication functions '''
import sys
import uuid
sys.path.append('libs')
from libs import crypto
import db

def login(login, password):
    ''' Check if the password is correct for the given user '''
    user_id = db.get_user_id(login)
    user_role = None
    if user_id is not None:
        hashed_password = crypto.hash_password(str(user_id) + password + str(user_id))
        user_role = db.get_user_role(user_id, hashed_password)
        if user_role is not None:
            new_uuid = str(uuid.uuid4())
            if(db.insert_new_token(new_uuid, user_role)):
                return new_uuid
            return 503
        else:
            return 403
    else:
        return 404