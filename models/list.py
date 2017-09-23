from peewee import *
from base_model import BaseModel

class List(BaseModel):

	name = CharField(max_length=150)