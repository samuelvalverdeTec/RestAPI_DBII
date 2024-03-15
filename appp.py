from flask import Flask, request, jsonify, make_response, render_template, session
import jwt
from datetime import datetime, timedelta
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd39a0c743d604dc0848b7e78ff428762'

#Home
def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request/args.get('token')
        if not token:
            return jsonify({'Alert!':'Token is missing!'})
        try:
            payload = jwt.encode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'Alert!':'Invalid Token!'})
    return decorated

#Public
@app.route('/public')
def public():
    return 'For Public'

#Authenticated
@app.route('/auth')
@token_required
def auth():
    return 'JWT is verified. Welcome to your dashboard!'


@app.route('/')
def home():
    if not session.get('logged in'):
        return render_template('login.html')
    else:
        return 'Logged in currently!'
    
@app.route('/login', methods=['POST'])
def login():
    if request. form['username'] and request.form['password'] == '123456':
        session['logged_in'] = True
        token = jwt.encode(
            {
                'user': request.form['username'],
                'expiration': str(datetime.utcnow() + timedelta(seconds=120))
            }, 
            app.config['SECRET_KEY']
        )
        return jsonify({'token': token})


    else:
        return make_response('Unable to verify', 403, {'WWW-Authenticate' : 'Basic realm: "Authentication Failed!"'})

if __name__ == "__main__":
    app.run(debug=True)