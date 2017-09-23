import jwt
import config
from flask import g

def auth_by_token(token):
    decoded = jwt.decode(token, config.JWT_SEC, algorithms=['HS256'])
    if decoded is None:
        return False
    else:
        g.user = decoded.get('user')
        return True
