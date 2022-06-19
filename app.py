''' Main program '''

from flask import Flask, request, Response, json
import db
import auth

app = Flask(__name__)

@app.before_first_request
def init():
    ''' Create the DB with tables and default data '''
    db.init()

@app.route('/', methods = ['GET'])
def default():
    ''' Healthcheck '''
    print('Healthcheck request made')
    return Response("{'Message':'It works!'}", status=200, mimetype='application/json')

@app.route('/login', methods = ['POST'])
def login():
    ''' POST request to perform login '''
    print('Login request made')
    try:
        data = json.loads(request.data)
        username = data["username"]
        password = data["password"]
        if username is not None:
            if password is not None:
                result = auth.login(username, password)
                if result in (403, 404):
                    return Response("{'Error':'Invalid username or password'}", status=403, mimetype='application/json')
                return Response('', status=200, mimetype='application/json')
            else:
                return Response("{'Error':'Missing password parameter'}", status=422, mimetype='application/json')
        else:
            return Response("{'Error':'Missing username parameter'}", status=422, mimetype='application/json')
    except:
        return Response("{'Error':'Message in invalid format'}", status=400, mimetype='application/json')

if __name__ == "__main__":
    app.run(host ='0.0.0.0')
