import jwt
import config

def auth_by_token(token):
    decoded = jwt.decode(token, config.JWT_SEC, algorithms=['SH256'])
    if decoded is None:
        return False
    else:
        return True
