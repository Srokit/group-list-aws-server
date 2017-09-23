from peewee import *
from base_model import BaseModel

class User(BaseModel):

	# Identifier
	phone_num = CharField(max_length=13)
	name = CharField(max_lenth=50)
	password_hashed = CharField(max_lenth=100)