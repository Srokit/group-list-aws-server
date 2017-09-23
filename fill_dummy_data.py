from models.base_model import db
from models.user import User
from models.list import List
from models.item import Item
from models.list_user import ListUser
from dummy_data import *

def fill_dummy_users():
    for dumb_user in dummy_users:
        print('Adding User:', dumb_user)
        User.create(phone_num=dumb_user.get('phone_num'), name=dumb_user.get('name'),
                    password_hashed=dumb_user.get('password_hashed'))

def fill_dummy_lists():
    for dumb_list in dummy_lists:
        print('Adding List:', dumb_list)
        List.create(name=dumb_list.get('name'))

def fill_dummy_items():
    for dumb_item in dummy_items:
        print('Adding Item:', dumb_item)
        Item.create(text=dumb_item.get('text'), is_checked=dumb_item.get('is_checked'),
                    list=dumb_item.get('list'))

def fill_dummy_list_users():
    for dumb_list_user in dummy_list_users:
        print('Adding ListUser:', dumb_list_user)
        ListUser.create(list=dumb_list_user.get('list'), user=dumb_list_user.get('user'))

def run():
    fill_dummy_users()
    fill_dummy_lists()
    fill_dummy_items()
    fill_dummy_list_users()

def setup_db():
    print('Opening DB')
    db.connect()
    print('Dropping existing DB data')
    db.drop_tables([User, List, Item, ListUser], safe=True)
    print('Create brand new tables')
    db.create_tables([User, List, Item, ListUser], safe=True)

def teardown():
    db.close()
    print('Closed DB')

if __name__ == '__main__':

    setup_db()
    run()
    teardown()

    print('DB Updated with dummy data!')
