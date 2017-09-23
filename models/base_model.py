from peewee import *
import config
from playhouse.db_url import connect

db = connect(config.SQL_DBURL)

class BaseModel(Model):

	class Meta:
		database = db