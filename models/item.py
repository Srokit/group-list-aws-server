from peewee import *
from .base_model import BaseModel
from .list import List


class Item(BaseModel):

	text = CharField(max_length=500)
	is_checked = BooleanField(default=False)
	list = ForeignKeyField(List)

	def to_dict_with_public_data(self):
		return {
			'text': self.text,
			'isChecked': self.is_checked,
			'id': self.id
		}


def fetch_items_for_list_with_id(items, list_id):
	return Item.select().where(Item.list == list_id)

def make_items_with_list_id(items, list_id):

	err_msg = "Could not make items with positions " # Append to this possibly

	one_not_created = False
	item_pos = 1
	for item in items:										# Can't start checked
		item_res = Item.create(text=item.get('text'), list_id=list_id, is_checked=False)
		if item_res is None:
			err_msg += "%d, " % item_pos
			one_not_created = True
		item_pos += 1

	if one_not_created:
		return jsonify({'success': False, 'errMsg': err_msg.strip(', ')})

	return jsonify({'success': True})
