
from flask import request, jsonify
from models.user import *

# PUT /api/user/
# Request that is made on user signup
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

# POST /api/user/
# Request that is made on user signin
#----BODY FORMAT-----
# {
#		phoneNum: 12345677,
#     	password: slfnoigneroign
# }
#

def post_route_user():

	phone_num = request.form.get('phone_num')
	password = request.form.get('password')

	if phone_num is None:
		return jsonify({'success': False, 'errMsg': 'No phone number provided'})

	success, user_public_data, err_msg = fetch_user_by_phone_num(phone_num, password)

	if success:
		return jsonify({'success': True, 'user': user_public_data})

	else:
		return jsonify({'success': False, 'errMsg': err_msg})
