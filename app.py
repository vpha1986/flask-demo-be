from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/getPersonInfo', methods=['GET'])
def get_person_info():
    return jsonify([
        {
        'name': 'John Doe',
        'age': 30,
        'email': 'johndoe@example.com'
        },
        {
        'name': 'Doe',
        'age': 40,
        'email': 'doej@example.com'
        },
        {
        'name': 'OneMore',
        'age': 30,
        'email': 'adoej@example.com'
        },
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0')
