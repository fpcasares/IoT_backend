from flask import request,Flask,jsonify
import os


if os.system('ps -A | grep pigpiod')==0:
    GPIO=True
#    from GPIO.IR.IREMIT import *

app = Flask(__name__)

@app.route('/api/v1', methods=['GET'])
def home():
     return('Main Page')


@app.route('/api/v1/available_scripts', methods=['GET'])
def get_available_scripts():
     script_list=glob.glob('/GPIO/**/*.py',recursive=True)
     return jsonify(script_list)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port='5009')
