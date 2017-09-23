from peewee import *
from .user import User
from .list import List

from .base_model import BaseModel


class ListUser(BaseModel):

	user = ForeignKeyField(User)
	list = ForeignKeyField(List)

def fetch_lists_for_phone_num(user_id):

	user = User.select().where(User.id == user_id).first()
	if user is None:
		return False, None, 'User with user_id %s does not exist' % user_id

	list_users = ListUser.select() \
		.join(User) \
		.switch(ListUser) \
		.join(List) \
		.where(ListUser.user == user.id)
	lists = [ list_user.list for list_user in list_users ]

	return True, lists, None
