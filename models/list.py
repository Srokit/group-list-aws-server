from peewee import *
from .base_model import BaseModel

class List(BaseModel):

	name = CharField(max_length=150)

	def to_dict_with_public_data(self):
		return {
			'name': self.name
		}
