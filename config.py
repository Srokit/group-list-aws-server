import os

SQL_DBURL=os.environ.get('SQL_DBURL')

SQL_HOST = os.environ.get('SQL_HOST')
SQL_PORT = os.environ.get('SQL_PORT')
SQL_DBNAME = os.environ.get('SQL_DBNAME')

if SQL_PORT is not None:
	SQL_PORT = int(SQL_PORT)

SQL_USER = os.environ.get('SQL_USER')
SQL_PASSWORD = os.environ.get('SQL_PASSWORD')

# On prod server this var will be set but not on local
if SQL_DBURL is None:
	SQL_DBURL = 'mysql://%s:%s@%s/%s' % (SQL_USER, SQL_PASSWORD, SQL_HOST, SQL_DBNAME)
print("Config.SQL_DBURL:", SQL_DBURL)

# For JWT
JWT_SEC = os.environ.get('JWT_SEC')
