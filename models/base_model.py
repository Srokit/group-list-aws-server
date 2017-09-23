from peewee import *
import config

db = MySQLDatabase('grouplistdatabase', host=config.SQL_HOST, port=config.SQL_PORT,
								   user=config.SQL_USER, password=config.SQL_PASSWORD)

class BaseModel(Model):

	class Meta:
		database = db