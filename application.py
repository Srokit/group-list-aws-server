from flask import Flask
from models.base_model import db
from models.item import Item
from models.list import List
from models.user import User
import pymysql

from routes.route_user import *

app = Flask(__name__)

@app.before_request
def _db_connect():
	db.connect()

@app.teardown_request
def _db_close(exc):
	if not db.is_closed():
		db.close()

@app.route('/')
def hello_world():
	return 'Hello world'

@app.route('/api/user', methods=['POST'])
def post_api_user():
	return post_route_user()

def setup_db():
	db.connect()
	db.create_tables([Item, List, User])
	db.close()

if __name__ == '__main__':

	setup_db()
	app.run()
