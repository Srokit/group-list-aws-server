
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

def put_route_user():

	post_body = request.form
	success, err_msg = make_user(post_body.get('phoneNum'), post_body.get('name'), post_body.get('password'))

	if success:
		return jsonify({'success': True})
	else:
		return jsonify({'success': False, 'errMsg': err_msg})

def get_route_user():

	phone_num = request.args.get('phone_num')

	if phone_num is None:
		return jsonify({'success': False, 'errMsg': 'No phone number provided'})

	user_public_data = fetch_user_by_phone_num(phone_num)

	if user_public_data is None:
		return jsonify({'success': False, 'errMsg': 'No user found with that phone number'})


	return jsonify({'success': True, 'user': user_public_data})