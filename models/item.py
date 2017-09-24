from peewee import *
from .base_model import BaseModel
from .list import List


class Item(BaseModel):

	text = CharField(max_length=500)
	is_checked = BooleanField(default=False)
	list = ForeignKeyField(List)
	creator = CharField(max_length=100)

	def to_dict_with_public_data(self):
		return {
			'text': self.text,
			'isChecked': self.is_checked,
			'id': self.id,
			'creator': self.creator
		}


def fetch_items_for_list_with_id(list_id):
	return Item.select().where(Item.list == list_id)

def fetch_item_with_id(item_id):
	return Item.select().where(Item.id == item_id).first()

def make_items_with_list_id(items, list_id):

	err_msg = "Could not make items with positions " # Append to this possibly

	one_not_created = False
	item_pos = 1
	item_reses = []
	for item in items:										# Can't start checked
		item_res = Item.create(text=item.get('text'), list=list_id, is_checked=False, creator=item.get('creator'))
		if item_res is None:
			err_msg += "%d, " % item_pos
			one_not_created = True
		else:
			item_reses.append(item_res)
		item_pos += 1

	if one_not_created:
		return False, None, err_msg.strip(', ')

	return True, item_reses, None

def delete_item_with_id(item_id):
	Item.delete().where(Item.id == item_id).execute()

	if Item.select().where(Item.id == item_id).first() is not None:
		return False, 'Item with id %d was not deleted' % item_id
	return True, None

def delete_items_with_list_id(list_id):

	Item.delete().where(Item.list == list_id).execute()

	if Item.select().where(Item.list == list_id).first() is not None:
		return False, 'All items under list with id %d were not deleted' % list_id
	return True, None


def edit_item(item):

	Item.update(text=item.get('text'), is_checked=item.get('isChecked')) \
		.where(Item.id == item.get('id')).execute()
