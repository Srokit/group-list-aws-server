import jwt
import config
from flask import g
import json
from models.loggedout_token import *

def auth_by_token(token):
    if is_token_in_loggedout_tokens(token):
        return False
    
    decoded = jwt.decode(token, config.JWT_SEC, algorithms=['HS256'])
    
    if decoded is None:
        return False
    else:
        g.user = decoded.get('user')
        return True


def get_request_body_data(request):

    if request.data is None or len(request.data) == 0:
        # Must be in request.form
        return request.form
    else:
        return json.loads(request.data)
