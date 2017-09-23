from peewee import *
from .base_model import BaseModel
from werkzeug.security import generate_password_hash

class User(BaseModel):

	# Identifier
	phone_num = CharField(max_length=13)
	name = CharField(max_length=50)
	password_hashed = CharField(max_length=100)

def make_user(phone_num, name, password):

	password_hashed = generate_password_hash(password)

	user, created = User.get_or_create(
		phone_num=phone_num,
		name=name,
		password_hashed=password_hashed
	)

	if not created:
		return False, 'Cannot create duplicate user with phone number: %s' % phone_num

	return True, None