from flask import request,Flask
import os


if os.system('ps -A | grep pigpiod')==0:
    GPIO=True
#    from GPIO.IR.IREMIT import *

app = Flask(__name__)


@app.route('/available_scripts', methods=['GET'])
def login():
     os.system("find /GPIO -name *.py")
     return 'Hello World'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port='5009')
