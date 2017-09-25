from peewee import *
from .base_model import BaseModel


class List(BaseModel):

	name = CharField(max_length=150)
	
	# todo: make FK
	creator = CharField(max_length=100) #I know this should be a FK everntually

	def to_dict_with_public_data(self):
		return {
			'name': self.name,
			'items': self.items,
			'users': self.users,
			'id': self.id,
			'creator': self.creator
		}

	def attach_items_as_dicts(self, items):
		self.items = [ item.to_dict_with_public_data() for item in items]

	def attach_users_as_dicts(self, users, ignore_user_id):
		self.users = [ user.to_dict_with_public_data() for user in users if user.id != ignore_user_id ]


def make_list(_list):
	new_list = List.create(name=_list.get('name'), creator=_list.get('creator'))
	if new_list is None:
		return False, None, 'Could not create list with name %s' % _list.get('name')
	return True, new_list.id, None


def delete_list_with_id(list_id):
	List.delete().where(List.id == list_id).execute()

def edit_list(_list):
	List.update(name=_list.get('name')) \
	    .where(List.id == _list.get('id')).execute()
