import jwt
import config
from flask import g

def jwt_authenticator(token):

    decoded = jwt.decode(token, config.JWT_SEC, algorithms=['SH256'])
    if decoded is not None:
        g.user = {
            # phoneNum to phone_num
            'phone_num': decoded.get('user').get('phoneNum'),
            'name': decoded.get('user').get('name')
        }
        return True, None

    return False, 'Forbidden'
