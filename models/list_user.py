from peewee import *
from .user import User
from .list import List

from .base_model import BaseModel


class ListUser(BaseModel):

	user = ForeignKeyField(User)
	list = ForeignKeyField(List)


def fetch_lists_for_user_with_id(user_id):
	list_users = (
		ListUser.select()
		.join(User)
		.switch(ListUser)
		.join(List)
		.where(ListUser.user == user_id)
	)
	
	lists = [ list_user.list for list_user in list_users ]

	return True, lists, None


def is_user_with_id_part_of_list_with_id(user_id, list_id):

	user = User.select().where(User.id == user_id).first()
	if user is None:
		return False, 'User with user_id %d does not exist' % user_id

	_list = List.select().where(List.id == list_id).first()
	if _list is None:
		return False, 'List with list_id %d does not exist' % list_id

	list_user = (
		ListUser.select(ListUser, User, List)
		.join(User)
		.switch(ListUser)
		.join(List)
		.where(ListUser.user == user_id, ListUser.list == list_id)
		.first()
	)

	if list_user is None:
		return False, 'User with id %d is not a part of list with id %d' % (user_id, list_id)

	return True, None

def make_user_with_id_apart_of_list_with_id(user_id, list_id):

	user = User.select().where(User.id == user_id).first()
	if user is None:
		return False, 'User with user_id %d does not exist' % user_id

	_list = List.select().where(List.id == list_id).first()
	if _list is None:
		return False, 'List with list_id %d does not exist' % list_id

	list_user = (
		ListUser.select(ListUser, User, List)
		.join(User)
		.switch(ListUser)
		.join(List)
		.where(ListUser.user == user_id, ListUser.list == list_id)
		.first()
	)

	if list_user is not None:
		return False, 'Cannot add user with id %d to list with id %d again' \
				% (user_id, list_id)

	ListUser.create(user=user_id, list=list_id)

	return True, None


def delete_list_user_with_list_id(list_id):
	ListUser.delete().where(ListUser.list == list_id).execute()


def get_users_apart_of_list_with_id(list_id):

	list_users = (
		ListUser.select()
		.join(User)
		.switch(ListUser)
		.join(List)
		.where(ListUser.list == list_id)
	)
	users = [ list_user.user for list_user in list_users ]

	return users
