
from flask import request, jsonify
from models.user import *

# POST /api/user/
# Request that is made on user signin
# ----BODY FORMAT----
# {
#		phoneNum: 12343445555,
#		name: absdfsdfjf,
#		password: slkdfnlkfn
# }
#

def post_route_user():

	post_body = request.form
	success, err_msg = make_user(post_body.get('phoneNum'), post_body.get('name'), post_body.get('password'))

	if success:
		return jsonify({'success': True})
	else:
		return jsonify({'success': False, 'errMsg': err_msg})