from .jwt_authenticator import jwt_authenticator
from models.list_user import *
from models.item import *

def get_route_list_all():

    if not g.has_jwt_token:
        return jsonify({'success': False, 'errMsg': 'Forbidden'})

    phone_num = g.user.get('phone_num')

    succeed, lists, err_msg = fetch_lists_for_phone_num(phone_num)

    for list in lists:
        items = fetch_items_for_list_with_id(list.id)
        lists_to_return.attach_items_as_dicts(items)

    lists_to_return = [ list.to_dict_with_public_data() for list in lists ]

    if succeed:
        return jsonify({'success': True, 'lists': lists_to_return})

    else:
        return jsonify({'success': False, 'errMsg': err_msg})
