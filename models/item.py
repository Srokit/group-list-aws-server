from peewee import *
from .base_model import BaseModel
from .list import List


class Item(BaseModel):

	text = CharField(max_length=500)
	is_checked = BooleanField(default=False)
	list = ForeignKeyField(List)


def fetch_items_for_list_with_id(list_id):
	return Item.select().where(Item.list == list_id)
