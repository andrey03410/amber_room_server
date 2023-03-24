from flask import Flask, jsonify, Response, request, make_response
from werkzeug.exceptions import HTTPException
import db_controller

app = Flask(__name__)
db = db_controller.DbController()


def build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add('Access-Control-Allow-Headers', "*")
    response.headers.add('Access-Control-Allow-Methods', "*")
    return response


def empty_response(status: int):
    response = Response(status=status)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.content_type = 'application/json'
    return response


@app.errorhandler(500)
def error_handler():
    response = Response(status=501)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.content_type = 'application/json'
    return response


@app.route('/getPersons', methods=['GET'])
def get_persons():
    persons = db.get_persons()
    response = jsonify({'persons': persons})
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.content_type = 'application/json'
    response.status = 200
    return response


@app.route('/addPerson', methods=['POST', 'OPTIONS'])
def add_person():
    if request.method == 'OPTIONS':
        return build_cors_preflight_response()
    elif request.method == "POST":
        data = request.get_json()
        db.add_person(data['name'], data['id_nationality'], data['description'])
        return empty_response(200)


if __name__ == '__main__':
    app.run(debug=True)
