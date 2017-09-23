from flask import Flask, request, g
from models.base_model import db
from models.item import Item
from models.list import List
from models.user import User
from models.list_user import ListUser
from models.loggedout_token import LoggedoutToken
import pymysql
from helpers import *

from routes.route_user import *
from routes.route_list import *
from routes.route_item import *


app = Flask(__name__)


def setup_db():
	db.connect()
	db.create_tables([User, List, Item, ListUser, LoggedoutToken], safe=True)


@app.before_request
def _db_connect():
	setup_db()
	jwt_token = request.args.get('jwt')
	if jwt_token is not None:
		g.has_jwt_token = auth_by_token(jwt_token)
	else:
		g.has_jwt_token = False


@app.teardown_request
def _db_close(exc):
	if not db.is_closed():
		db.close()


@app.route('/api/user', methods=['PUT'])
def put_api_user():
	return put_route_user()


@app.route('/api/user', methods=['POST'])
def post_api_user():
	return post_route_user()


@app.route('/api/user', methods=['PATCH'])
def patch_api_user():
	return patch_route_user()


@app.route('/api/list/all', methods=['GET'])
def get_api_list_all():
	return get_route_list_all()


@app.route('/api/items', methods=['PUT'])
def put_api_items():
	return put_route_items()


if __name__ == '__main__':
	app.run()
