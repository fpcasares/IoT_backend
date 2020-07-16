from flask import Flask, session, redirect, url_for, request, request, jsonify
from markupsafe import escape
import os


if os.system('ps -A | grep pigpiod')==0:
    GPIO=True
    from GPIO.IR.IREMIT import *

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = os.urandom(16)


@app.route('/api/auth')
def auth():
    json_data = request.get_json()
    email = json_data['email']
    password = json_data['password']
    return jsonify(token=generate_token(email, password))

with app.test_client() as c:
    rv = c.post('/api/auth', json={
        'email': 'flask@example.com', 'password': 'secret'
    })
    json_data = rv.get_json()
    assert verify_token(email, json_data['token'])
    
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5003)
