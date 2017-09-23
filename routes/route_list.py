from .jwt_authenticator import jwt_authenticator
from models.list_user import *

def get_route_list_all():

    phone_num = g.user.get('user_name')

    succeed, lists, err_msg = fetch_lists_for_phone_num(phone_num)

    if succeed:
        return jsonify({'success': True, 'lists': lists})

    else:
        return jsonify({'success': False, 'errMsg': err_msg})
