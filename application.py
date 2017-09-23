from flask import Flask

flask_app = Flask(__name__)

@flask_app.route('/')
def hello_world():
    return 'Hello world'

if __name__ == '__main__':

  flask_app.run(debug=True)
