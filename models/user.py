from peewee import *
from .base_model import BaseModel
from werkzeug.security import generate_password_hash

class User(BaseModel):

	# Identifier
	phone_num = CharField(max_length=13)
	name = CharField(max_length=50)
	password_hashed = CharField(max_length=100)

	def to_dict_with_public_data(self):
		return {
			'phoneNum': self.phone_num,
			'name': self.name
		}

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

def fetch_user_by_phone_num(phone_num):

	user = User.select().where(User.phone_num == phone_num).limit(1).first()

	if user is None:
		return None

	return user.to_dict_with_public_data()

