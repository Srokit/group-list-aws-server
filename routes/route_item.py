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

    user_id = g.user.get('id')

    put_data = json.loads(request.data)

    items = put_data['items']
    list_id = put_data['listId']

    success, err_msg = is_user_with_id_part_of_list_with_id(user_id, list_id)

    if not success:
        return jsonify({'success': False, 'errMsg': err_msg})

    success, err_msg = make_items_with_list_id(items, list_id)

    if not success:
        return jsonify({'success': False, 'errMsg': err_msg})

    return jsonify({'success': True})
