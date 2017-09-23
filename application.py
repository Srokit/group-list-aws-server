from flask import Flask
from models.base_model import db
from models.item import Item
from models.list import List
from models.user import User
from models.list_user import ListUser
from models.loggedout_token import LoggedoutToken
import pymysql

from routes.route_user import *
from routes.route_list import *

app = Flask(__name__)

def setup_db():
	db.connect()
	db.create_tables([User, List, Item, ListUser, LoggedoutToken], safe=True)

@app.before_request
def _db_connect():
	setup_db()

@app.teardown_request
def _db_close(exc):
	if not db.is_closed():
		db.close()

@app.route('/')
def hello_world():
	return 'Hello world'

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

if __name__ == '__main__':
	app.run()
