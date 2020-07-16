from flask import request
import os


if os.system('ps -A | grep pigpiod')==0:
    GPIO=True
    from GPIO.IR.IREMIT import *

app = Flask(__name__)


@app.route('/available_scripts', methods=['GET'])
def login():
    return get scripts()



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port='5009')
