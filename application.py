from flask import Flask
from models.base_model import db
from models.item import Item
from models.list import List
from models.user import User
from models.list_user import ListUser
import pymysql

from routes.route_user import *

app = Flask(__name__)

def setup_db():
	db.connect()
	db.create_tables([User, List, Item, ListUser], safe=True)

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

@app.route('/api/user', methods=['GET'])
def get_api_user():
	return get_route_user()

if __name__ == '__main__':
	app.run()
