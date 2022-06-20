''' Main program '''

from flask import Flask, request, Response, json
import db
import auth
import externalcontent
from libs.utils import get_consumer_from_db

app = Flask(__name__)

@app.before_first_request
def init():
    ''' Create the DB with tables and default data '''
    db.init()
    externalcontent.get_external_data()

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
                elif result == 503:
                    return Response("{'Error':'Server error while generating the token'}", status=503, mimetype='application/json')
                return Response("{'token':'" + result + "'}", status=200, mimetype='application/json')
            else:
                return Response("{'Error':'Missing password parameter'}", status=422, mimetype='application/json')
        else:
            return Response("{'Error':'Missing username parameter'}", status=422, mimetype='application/json')
    except:
        return Response("{'Error':'Message in invalid format'}", status=400, mimetype='application/json')

@app.route('/consumer', methods = ['GET'])
def search():
    ''' GET request to obtain a consumer from the DB '''
    token = request.headers.get('token')
    role = auth.get_role_from_token(token)

    if role == 403:
        return Response("{'Error':'Invalid authentication token'}", status=403, mimetype='application/json')

    consumer_id = request.args.get('id')
    consumer_username = request.args.get('username')
    consumer = None

    if consumer_id is not None:
        consumer = get_consumer_from_db("ID", consumer_id, role)
    elif consumer_username is not None:
        consumer = get_consumer_from_db("username", consumer_username, role)

    if consumer == 404:
        return Response("{'Error':'Consumer not found'}", status=404, mimetype='application/json')
    elif consumer == 422:
        return Response("{'Error':'The server had a problem processing the request'}", status=422, mimetype='application/json')
    elif consumer is None:
        return Response("{'Error':'Missing id or username arguments (lowercase only)'}", status=422, mimetype='application/json')
    else:
        return Response(consumer, status=200, mimetype='application/json')

if __name__ == "__main__":
    app.run(host ='0.0.0.0')
