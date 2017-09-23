from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

if __name__ == '__main__':

  app.run(port=os.environ.get('PORT'))
