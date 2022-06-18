import db
import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def default():
    return 'PING'

@app.route('/initdb')
def db_init():
  db.init()
  return 'init database'

if __name__ == "__main__":
  app.run(host ='0.0.0.0')