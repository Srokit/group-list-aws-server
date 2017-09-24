from flask import g, jsonify
from models.list_user import *
from models.item import *

def get_route_list_all():

    if not g.has_jwt_token:
        return jsonify({'success': False, 'errMsg': 'Forbidden'})

    user_id = g.user.get('id')

    succeed, lists, err_msg = fetch_lists_for_user_with_id(user_id)

    if not succeed:
        return jsonify({'success': False, 'errMsg': err_msg})

    for _list in lists:
        items = fetch_items_for_list_with_id(_list.id)

        _list.attach_items_as_dicts(items)

    lists_to_return = [ _list.to_dict_with_public_data() for _list in lists ]

    if succeed:
        return jsonify({'success': True, 'lists': lists_to_return})

    else:
        return jsonify({'success': False, 'errMsg': err_msg})
