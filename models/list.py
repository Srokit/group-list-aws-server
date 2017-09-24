from peewee import *
from .base_model import BaseModel


class List(BaseModel):

	name = CharField(max_length=150)

	def to_dict_with_public_data(self):
		return {
			'name': self.name,
			'item': self.items,
			'id': self.id
		}

	def attach_items_as_dicts(self, items):
		self.items = [ item.to_dict_with_public_data() for item in items]


def make_list(_list):
	new_list = List.create(name=_list.get('name'))
	if new_list is None:
		return False, None, 'Could not create list with name %s' % _list.get('name')
	return True, new_list.id, None
