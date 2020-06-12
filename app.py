from flask import Flask
import redis

app = Flask(__name__)
app.config['SECRET_KEY'] = '8u3rouhfkjdsfiluh'

db = redis.Redis('localhost')

from routes import *

if __name__ == '__main__':
    app.run(debug=True)
