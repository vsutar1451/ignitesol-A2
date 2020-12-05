from flask import Flask,request, render_template
from flask import jsonify
app = Flask(__name__)
app.config.from_object("config.Config")
from flask import json
from werkzeug.exceptions import HTTPException
import random
import string
import math


app = Flask(__name__)
app.config.from_object("config.Config")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(HTTPException)
def handle_exception(e):
    response = e.get_response()
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"

    return response

@app.route('/hello',methods=['GET','POST'])
def index():
    try:
        dict = {"hindi":"Namastey sansar","english":"Hello world","french":"Bonjour le monde"}
        lang = request.args.get('language').lower()
        result_str=""
        letters = string.ascii_uppercase
        result_str = ''.join(random.choice(letters) for i in range(1))
        digits = [i for i in range(0, 10)]
        for i in range(9):
            index = math.floor(random.random() * 10)
            result_str += str(digits[index])
        print(result_str)
        if lang in dict:
            data={}
            data['Message ID']=result_str
            data['Message_text']=dict[lang]
            return jsonify(data)  
        else:
            data1={}
            data1['error_message']="The requested language is not supported"
            return jsonify(data1)
    except Exception as error:
        print('In exception :', error)
        return error





if __name__ == '__main__':
    app.run(debug=True)
