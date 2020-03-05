#importing necessary libraries
from flask import Flask, jsonify, request
from library import *
app = Flask(__name__)
@app.route('/chat',methods=['POST'])
def predict_by_natural_language_processing():
    raw_data = request.json
    raw_data["answer "] = pre_processing(raw_data["question"])
    return raw_data

#seeting name to run this file as flask app
if __name__ == '__main__':
    app.run(debug=True)