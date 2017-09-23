from .jwt_authenticator import jwt_authenticator
from models.list_user import *

def get_route_list_all():

    phone_num = g.user.get('phone_num')

    succeed, lists, err_msg = fetch_lists_for_phone_num(phone_num)

    lists_to_return = [ list.to_dict_with_public_data() for list in lists ]

    if succeed:
        return jsonify({'success': True, 'lists': lists_to_return})

    else:
        return jsonify({'success': False, 'errMsg': err_msg})
