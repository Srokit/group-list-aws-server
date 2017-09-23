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

def is_user_with_id_part_of_list_with_id(user_id, list_id):

	user = User.select().where(User.id == user_id).first()
	if user is None:
		return False, 'User with user_id %d does not exist' % user_id

	_list = List.select().where(List.id == list_id).first()
	if _list is None:
		return False, 'List with list_id %d does not exist' % list_id

	list_user = ListUser.select(User, List).where(User.id == user_id and List.id == list_id).first()

	if list_user is None:
		return False, 'User with id %d is not a part of list with id %d' % (user_id, list_id)

	return True, None
