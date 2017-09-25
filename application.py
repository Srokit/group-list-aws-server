from flask import Flask, request, g
from flask_httpauth import HTTPBasicAuth
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from models.base_model import db
from helpers import *

from routes.route_user import *
from routes.route_list import *
from routes.route_item import *


app = Flask(__name__)

auth = HTTPBasicAuth()

#limits how many requests can come from an address i think
limiter = Limiter(app, key_func=get_remote_address, default_limits=["1000 per hour"])


def setup_db():
	db.connect()
	db.create_tables([User, List, Item, ListUser, LoggedoutToken], safe=True)


@auth.error_handler
def auth_error():
	return "Access Denied"


@app.before_request
def _db_connect():
	#setup_db()
	
	db.connect()
	
	jwt_token = request.args.get('jwt')
	if jwt_token is not None:
		g.has_jwt_token = auth_by_token(jwt_token)
	else:
		g.has_jwt_token = False
		
	g.jwt_token = jwt_token
	# Can access this dict for all json posts now no matter if
	# form encoded or nah
	g.body = get_request_body_data(request)


@app.teardown_request
def _db_close(exc):
	if not db.is_closed():
		db.close()


# PUT is sign up, POST is login
@app.route('/api/user', methods=['PUT', 'POST', 'PATCH'])
def put_api_user():
	if request.method == 'PUT':
		return put_route_list()
	
	if request.method == 'POST':
		return post_route_user()
	
	if request.method == 'PATCH':
		return patch_route_user()
	
	return put_route_user()


@app.route('/api/list/all', methods=['GET'])
def get_api_list_all():
	return get_route_list_all()


@app.route('/api/list', methods=['PUT', 'PATCH', 'DELETE'])
def put_api_list():
	if request.method == 'PUT':
		return put_route_list()
	
	if request.method == 'PATCH':
		return patch_route_list()
	
	if request.method == 'DELETE':
		return delete_route_list()


@app.route('/api/items', methods=['PUT'])
def put_api_items():
	return put_route_items()


# never creates individual items, only a list
@app.route('/api/item', methods=['PATCH', 'DELETE'])
def delete_api_item():
	if request.method == 'PATCH':
		return patch_route_item()
	
	if request.method == 'DELETE':
		return delete_route_item()
	
	

if __name__ == '__main__':
	app.run(debug=False, threaded=True)
