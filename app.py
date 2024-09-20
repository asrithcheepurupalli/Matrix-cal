from flask import Flask, request, render_template, jsonify
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    matrix_a = np.array(data['matrix_a'])
    matrix_b = np.array(data['matrix_b'])
    operation = data['operation']

    if operation == 'add':
        result = matrix_a + matrix_b
    elif operation == 'subtract':
        result = matrix_a - matrix_b
    elif operation == 'multiply':
        result = matrix_a.dot(matrix_b)
    else:
        return jsonify({'error': 'Invalid operation'})

    return jsonify({'result': result.tolist()})

if __name__ == '__main__':
    app.run(debug=True)
