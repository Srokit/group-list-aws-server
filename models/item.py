from peewee import *
from base_model import BaseModel

class Item(BaseModel):

	text = CharField(max_length=500)
	is_checked = BooleanField(default=False)