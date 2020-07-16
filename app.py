from flask import Flask, session, redirect, url_for, request
from markupsafe import escape
import os


if os.system('ps -A | grep pigpiod')==0:
    GPIO=True
    from GPIO.IR.IREMIT import *

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = os.urandom(16)

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as {}:{}'.format(escape(session['username']),escape(session['password']))
        
    else:
        return redirect(url_for('login'))
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        session['password'] = request.form['password']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))
    
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5003)
