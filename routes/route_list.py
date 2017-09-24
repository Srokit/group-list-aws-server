from flask import g, jsonify, request
import json
from models.list_user import *
from models.item import *
from models.list import *

def get_route_list_all():

    if not g.has_jwt_token:
        return jsonify({'success': False, 'errMsg': 'Forbidden'})

    user_id = g.user.get('id')

    succeed, lists, err_msg = fetch_lists_for_user_with_id(user_id)

    if not succeed:
        return jsonify({'success': False, 'errMsg': err_msg})

    for _list in lists:
        items = fetch_items_for_list_with_id(_list.id)
        users = get_users_apart_of_list_with_id(_list.id)

        _list.attach_items_as_dicts(items)
        _list.attach_users_as_dicts(users, user_id)

    lists_to_return = [ _list.to_dict_with_public_data() for _list in lists ]

    if succeed:
        return jsonify({'success': True, 'lists': lists_to_return})

    else:
        return jsonify({'success': False, 'errMsg': err_msg})


def put_route_list():

    if not g.has_jwt_token:
        return jsonify({'success': False, 'errMsg': 'Forbidden'})

    put_data = g.body
    user_name = g.user.get('name')

    _list = { 'name': put_data['name'],
        'creator': user_name
    }
    items = put_data['items']

    success, list_id, err_msg = make_list(_list)

    user_id = g.user.get('id')

    success, err_msg = make_items_with_list_id(items, list_id)

    if not success:
        return jsonify({'success': False, 'errMsg': err_msg})

    success, err_msg = make_user_with_id_apart_of_list_with_id(user_id, list_id)

    if not success:
        return jsonify({'success': False, 'errMsg': err_msg})

    new_list = _list
    new_list['id'] = list_id
    new_list['items'] = []
    return jsonify({'success': True, 'list': new_list})


def delete_route_list():

    if not g.has_jwt_token:
        return jsonify({'success': False, 'errMsg': 'Forbidden'})

    user_id = g.user.get('id')

    list_id = int(request.args.get('listId'))

    success, err_msg = is_user_with_id_part_of_list_with_id(user_id, list_id)

    if not success:
        return jsonify({'success': False, 'errMsg': err_msg})

    success, err_msg = delete_items_with_list_id(list_id)

    if not success:
        return jsonify({'success': False, 'errMsg': err_msg})

    delete_list_user_with_list_id(list_id)

    delete_list_with_id(list_id)

    return jsonify({'success': True})


def patch_route_list():

    if not g.has_jwt_token:
        return jsonify({'success': False, 'errMsg': 'Forbidden'})

    user_id = g.user.get('id')

    _list = g.body

    success, err_msg = is_user_with_id_part_of_list_with_id(user_id, _list['id'])

    if not success:
        return jsonify({'success': False, 'errMsg': err_msg})

    edit_list(_list)

    return jsonify({'success': True})
