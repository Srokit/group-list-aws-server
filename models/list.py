from peewee import *
from .base_model import BaseModel


class List(BaseModel):

	name = CharField(max_length=150)

	def to_dict_with_public_data(self):
		return {
			'name': self.name,
			'item': self.items
		}

	def attach_items_as_dicts(self, items):
		self.items = [ item.to_dict_with_public_data() for item in items]
