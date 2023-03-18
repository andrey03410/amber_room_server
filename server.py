from flask import Flask, jsonify, Response
import json

app = Flask(__name__)


@app.route('/getPersons', methods=['GET'])
def get_persons():
    persons = [{'id': 1, 'name': 'test1', 'description': 'testdesc1', 'id_nationality': 1},
               {'id': 2, 'name': 'test1', 'description': 'testdesc1', 'id_nationality': 1}]
    response = Response(response=json.dumps({'persons': persons}), status=200, headers=None,
                        content_type='application/json')
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response


@app.route('/addPerson', methods=['POST'])
def add_person():
    print("Персона добавлена")
    return "test"


if __name__ == '__main__':
    app.run(debug=True)
