
from flask import request, jsonify
from models.user import *
from models.loggedout_token import *
import jwt
import config
import datetime

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
# Will return a jsonwebtoken do identify user for subsequent requests
#----BODY FORMAT-----
# {
#		phoneNum: 12345677,
#     	password: slfnoigneroign
# }
#

def post_route_user():

	phone_num = request.form.get('phoneNum')
	password = request.form.get('password')

	if phone_num is None:
		return jsonify({'success': False, 'errMsg': 'No phone number provided'})

	success, user_public_data, err_msg = fetch_user_by_credentials(phone_num, password)

	if success:

		jwt_token = jwt.encode({'user': user_public_data, 'iat': datetime.datetime.now()}, config.JWT_SEC, algorithm='HS256').decode('utf-8')
		return jsonify({'success': True, 'jwt': jwt_token})

	else:
		return jsonify({'success': False, 'errMsg': err_msg})

# PATCH /api/user/
# Request that is made on user signout
# ----NO BODY----

def patch_route_user():

	if not g.has_jwt_token:
		return jsonify({'success': False, 'errMsg': 'Forbidden'})

	success, err_msg = make_loggedout_token_if_new(jwt_token)

	if success:
		return jsonify({'success': True})
	else:
		return jsonify({'success': False, 'errMsg': err_msg})
