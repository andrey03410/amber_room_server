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

@app.route('/getPlaces', methods=['GET'])
def get_places():
    places = db.get_places()
    response = jsonify({'places': places})
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.content_type = 'application/json'
    response.status = 200
    return response

@app.route('/getVersions', methods=['GET'])
def get_versions():
    versions = db.get_versions()
    response = jsonify({'versions': versions})
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.content_type = 'application/json'
    response.status = 200
    return response

@app.route('/getSearchAtt', methods=['GET'])
def get_search_attempts():
    search_attempts = db.get_search_attempts()
    response = jsonify({'search_attempts': search_attempts})
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.content_type = 'application/json'
    response.status = 200
    return response

@app.route('/getFinds', methods=['GET'])
def get_finds():
    find = db.get_finds()
    response = jsonify({'find': find})
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.content_type = 'application/json'
    response.status = 200
    return response

@app.route('/getDocument', methods=['GET'])
def get_document():
    document = db.get_document()
    response = jsonify({'document': document})
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.content_type = 'application/json'
    response.status = 200
    return response

@app.route('/getIndication', methods=['GET'])
def get_indication():
    indications = db.get_indication()
    response = jsonify({'indications': indications})
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.content_type = 'application/json'
    response.status = 200
    return response

@app.route('/getResearch', methods=['GET'])
def get_research():
    research = db.get_research()
    response = jsonify({'research': research})
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
