from flask import Flask, jsonify, Response, request, make_response, send_file
from flask_cors import CORS
import db_controller
import os
import json

app = Flask(__name__)
CORS(app)
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


@app.route('/getNationality', methods=['GET'])
def get_nationality():
    nationality = db.get_nationality()
    response = jsonify({'nationality': nationality})
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.content_type = 'application/json'
    response.status = 200
    return response


@app.route('/getTypeDoc', methods=['GET'])
def get_type_doc():
    type_doc = db.get_type_doc()
    response = jsonify({'type_doc': type_doc})
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.content_type = 'application/json'
    response.status = 200
    return response


@app.route('/getOrganisation', methods=['GET'])
def get_organisation():
    organisation = db.get_organisation()
    response = jsonify({'organisation': organisation})
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.content_type = 'application/json'
    response.status = 200
    return response


@app.route('/getTypeResearch', methods=['GET'])
def get_type_research():
    type_research = db.get_type_research()
    response = jsonify({'type_research': type_research})
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.content_type = 'application/json'
    response.status = 200
    return response


@app.route('/findDoc', methods=['POST', 'OPTIONS'])
def find_document():
    if request.method == 'OPTIONS':
        return build_cors_preflight_response()
    elif request.method == "POST":
        data = request.get_json()
        document_person = db.get_document_person()
        id_documents = []
        for item in document_person:
            if item['id_person'] == data['id_person']:
                id_documents.append(item['id_document'])
        documents = list(filter(lambda x: x['id'] in id_documents, db.get_document()))
        response = jsonify({'documents': documents})
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.content_type = 'application/json'
        response.status = 200
        if len(id_documents) == 0:
            response.status = 404
        return response


@app.route('/getImage<id>', methods=['GET'])
def get_image(id):
    documents = db.get_document()
    path = ''
    for item in documents:
        if item['id'] == int(id):
            path = item['path']
            break
    print('Путь до файла с БД:' + path)
    return send_file(path, mimetype='image/pdf')


@app.route('/addPerson', methods=['POST', 'OPTIONS'])
def add_person():
    if request.method == 'OPTIONS':
        return build_cors_preflight_response()
    elif request.method == "POST":
        data = request.get_json()
        db.add_person(data['name'], data['id_nationality'], data['description'])
        return empty_response(200)


@app.route('/addPlace', methods=['POST', 'OPTIONS'])
def add_place():
    if request.method == 'OPTIONS':
        return build_cors_preflight_response()
    elif request.method == "POST":
        data = request.get_json()
        db.add_place(data['name'], data['description'])
        return empty_response(200)


@app.route('/addVersion', methods=['POST', 'OPTIONS'])
def add_version():
    if request.method == 'OPTIONS':
        return build_cors_preflight_response()
    elif request.method == "POST":
        data = request.get_json()
        db.add_version(data['id_places'], data['description'])
        return empty_response(200)


@app.route('/addSearchAttempt', methods=['POST', 'OPTIONS'])
def add_search_attempts():
    if request.method == 'OPTIONS':
        return build_cors_preflight_response()
    elif request.method == "POST":
        data = request.get_json()
        db.add_search_attempts(data['id_versions'], data['date_start'], data['date_finish'], data['description'])
        return empty_response(200)


@app.route('/addFinds', methods=['POST', 'OPTIONS'])
def add_finds():
    if request.method == 'OPTIONS':
        return build_cors_preflight_response()
    elif request.method == "POST":
        data = request.get_json()
        db.add_finds(data['name'], data['id_search_attempts'], data['description'])
        return empty_response(200)


@app.route('/addResearches', methods=['POST', 'OPTIONS'])
def add_researches():
    if request.method == 'OPTIONS':
        return build_cors_preflight_response()
    elif request.method == "POST":
        data = request.get_json()
        db.add_researches(data['id_organization'], data['id_search_attempts'], data['description'],
                          data['id_type_research'], data['local_place'], data['technique'])
        return empty_response(200)


@app.route('/addIndications', methods=['POST', 'OPTIONS'])
def add_indications():
    if request.method == 'OPTIONS':
        return build_cors_preflight_response()
    elif request.method == "POST":
        data = request.get_json()
        db.add_indications(data['id_persons'], data['testimony'], data['id_versions'],
                           data['date'], data['id_documents'])
        return empty_response(200)


@app.route('/addDocument', methods=['POST'])
def add_document():
    if 'file' not in request.files:
        return empty_response(400)
    file = request.files['file']
    form = json.loads(request.form['data'])
    folder = app.config['UPLOAD_FOLDER']

    if os.path.isdir(folder): # проверка: запущена программа через ide или с помощью exe файла (потом пофиксить чтобы была единая папка)
        pass
    else:
        folder = app.config['UPLOAD_FOLDER2']

    if file:
        count = db.get_document_amount() + 1
        while True:
            filename = str(count) + '.pdf'
            print('Проверка файла ' + folder + '/' + filename)
            if os.path.isfile(folder + '/' + filename):
                count += 1
            else:
                break

        print('Создание файла в: ' + folder + '/' + filename)
        file.save(os.path.join(folder, filename))
        db.add_document(form['id_type_doc'], form['id_search_attempts'], form['date'], form['description'],
                        form['id_author'], form['id_person'], app.config['UPLOAD_FOLDER'] + '/' + filename)
        return empty_response(200)
    else:
        return empty_response(400)


if __name__ == '__main__':
    app.config['UPLOAD_FOLDER'] = 'docs'
    app.config['UPLOAD_FOLDER2'] = '_internal/docs'
    app.run(debug=True)
