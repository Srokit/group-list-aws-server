
from werkzeug.security import generate_password_hash

# Helper to select the primary key value for dummy data arrays based off index
def parse_primary_key(dummy_arr, key, val):
    for i, dumb_ele in enumerate(dummy_arr):
        if dumb_ele.get(key) is not None and dumb_ele.get(key) == val:
            return i + 1
    raise Exception('No matching %s:%s on dummy_array' % (key, val))

dummy_users = [
    {
        'phone_num': '15551234567',
        'name': 'Johnathan Shiii',
        'password_hashed': generate_password_hash('JohnathanPass')
    },
    {
        'phone_num': '15551237654',
        'name': 'Shaef Daddy',
        'password_hashed': generate_password_hash('ShaefPass')
    },
    {
        'phone_num': '15551234565',
        'name': 'Neilander Sehkon',
        'password_hashed': generate_password_hash('NeilanderPass')
    },
    {
        'phone_num': '15550004567',
        'name': 'Stanley Yelnats',
        'password_hashed': generate_password_hash('StanleyPass')
    },
    {
        'phone_num': '15551111567',
        'name': 'John Doe',
        'password_hashed': generate_password_hash('JohnPass')
    }
]

dummy_lists = [
    {
        'name': 'Todo List'
    },
    {
        'name': 'Grocery Supplies'
    },
    {
        'name': 'Bands we still need to see'
    },
    {
        'name': 'Vocab quiz words and definitions'
    },
    {
        'name': 'My best friendz'
    }
]

dummy_items = [
    {
        'text': 'Wash dishes',
        'is_checked': False,
        'list': parse_primary_key(dummy_lists, 'name', 'Todo List')
    },
    {
        'text': 'Do laundry',
        'is_checked': True,
        'list': parse_primary_key(dummy_lists, 'name', 'Todo List')
    },
    {
        'text': 'Solve a rubiks cube',
        'is_checked': False,
        'list': parse_primary_key(dummy_lists, 'name', 'Todo List')
    },
    {
        'text': 'Eggs',
        'is_checked': False,
        'list': parse_primary_key(dummy_lists, 'name', 'Grocery Supplies')
    },
    {
        'text': 'Bacon',
        'is_checked': False,
        'list': parse_primary_key(dummy_lists, 'name', 'Grocery Supplies')
    },
    {
        'text': 'Blink-182',
        'is_checked': False,
        'list': parse_primary_key(dummy_lists, 'name', 'Bands we still need to see')
    },
    {
        'text': 'Rae Sremmurd',
        'is_checked': True,
        'list': parse_primary_key(dummy_lists, 'name', 'Bands we still need to see')
    },
    {
        'text': 'J Beibs',
        'is_checked': True,
        'list': parse_primary_key(dummy_lists, 'name', 'Bands we still need to see')
    },
    {
        'text': 'Leviosa',
        'is_checked': False,
        'list': parse_primary_key(dummy_lists, 'name', 'Vocab quiz words and definitions')
    },
    {
        'text': 'Neilander baby',
        'is_checked': True,
        'list': parse_primary_key(dummy_lists, 'name', 'My best friendz')
    }
]

dummy_list_users = [
    {
        'list': parse_primary_key(dummy_lists, 'name', 'Todo List'),
        'user': parse_primary_key(dummy_users, 'name', 'Johnathan Shiii')
    },
    {
        'list': parse_primary_key(dummy_lists, 'name', 'Todo List'),
        'user': parse_primary_key(dummy_users, 'name', 'Shaef Daddy')
    },
    {
        'list': parse_primary_key(dummy_lists, 'name', 'Grocery Supplies'),
        'user': parse_primary_key(dummy_users, 'name', 'Johnathan Shiii')
    },
    {
        'list': parse_primary_key(dummy_lists, 'name', 'Todo List'),
        'user': parse_primary_key(dummy_users, 'name', 'John Doe')
    },
    {
        'list': parse_primary_key(dummy_lists, 'name', 'Todo List'),
        'user': parse_primary_key(dummy_users, 'name', 'Stanley Yelnats')
    },
    {
        'list': parse_primary_key(dummy_lists, 'name', 'Bands we still need to see'),
        'user': parse_primary_key(dummy_users, 'name', 'Johnathan Shiii')
    },
    {
        'list': parse_primary_key(dummy_lists, 'name', 'Bands we still need to see'),
        'user': parse_primary_key(dummy_users, 'name', 'Neilander Sehkon')
    }
]
