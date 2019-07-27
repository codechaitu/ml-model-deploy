import pickle
from flask import Flask, request, jsonify
import ast
import numpy as np

app = Flask(__name__)
port = 5000

model = pickle.load(open('model.pkl', 'rb'), encoding='latin1')


@app.route('/')
def index():
	return "Hello"

@app.route('/predict', methods=['GET', 'POST'])
def predict():
	print('entereed')
	input = request.args.get('input')
	print(type(input))
	input = ast.literal_eval(input)
	print(type(input))
	prediction = model.predict([input])
	response = {'prediction': np.array2string(prediction)}
	print(response)
	return jsonify(response)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port = port)
