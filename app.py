''' Main program '''

from flask import Flask
import db

app = Flask(__name__)

@app.before_first_request
def init():
    ''' Create the DB with tables and default data '''
    db.init()

@app.route('/')
def default():
    ''' Healthcheck '''
    return 'It works!'

if __name__ == "__main__":
    app.run(host ='0.0.0.0')
