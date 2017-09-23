from peewee import *
from .user import User
from .list import List

from .base_model import BaseModel

class ListUser(BaseModel):

	user = ForeignKeyField(User)
	list = ForeignKeyField(List)
