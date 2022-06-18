import db
from flask import Flask

app = Flask(__name__)

@app.before_first_request
def init():
  db.init()

@app.route('/')
def default():
    return 'It works!'

if __name__ == "__main__":
  app.run(host ='0.0.0.0')