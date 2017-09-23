from flask import Flask
from models.base_model import db
import pymysql

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

if __name__ == '__main__':

  app.run()
