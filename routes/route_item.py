import json
from flask import request, g, jsonify
from models.item import *
from models.list_user import *

# PUT /api/items/
# Request here when new items are done being added to a list from the user
# ----BODY FORMAT----
# {"items": [{
#   "id": integer,
#   "text": string
# },,...], "list_id": integer}
#

def put_route_items():

    if not g.has_jwt_token:
        return jsonify({'success': False, 'errMsg': 'Forbidden'})

    user_id = g.user.get('id')

    put_data = g.body

    items = put_data['items']
    list_id = put_data['listId']

    success, err_msg = is_user_with_id_part_of_list_with_id(user_id, list_id)

    if not success:
        return jsonify({'success': False, 'errMsg': err_msg})

    success, err_msg = make_items_with_list_id(items, list_id)

    if not success:
        return jsonify({'success': False, 'errMsg': err_msg})

    return jsonify({'success': True})

def delete_route_item():

    if not g.has_jwt_token:
        return jsonify({'success': False, 'errMsg': 'Forbidden'})

    user_id = g.user.get('id')
    item_id = int(request.args.get('itemId'))

    item = fetch_item_with_id(item_id)
    list_id = item.list.id
    success, err_msg = is_user_with_id_part_of_list_with_id(user_id, list_id)

    if not success:
        return jsonify({'success': False, 'errMsg': err_msg})

    succeed, err_msg = delete_item_with_id(item_id)

    if not succeed:
        return jsonify({'success': False, 'errMsg': err_msg})

    return jsonify({'success': True})

def patch_route_item():

    if not g.has_jwt_token:
        return jsonify({'success': False, 'errMsg': 'Forbidden'})

    user_id = g.user.get('id')
    item_dict = g.body

    item = fetch_item_with_id(int(item_dict.get('id')))
    list_id = item.list.id
    success, err_msg = is_user_with_id_part_of_list_with_id(user_id, list_id)

    if not success:
        return jsonify({'success': False, 'errMsg': err_msg})

    edit_item(item_dict)

    return jsonify({'success': True})
