from flask import Flask, jsonify, Response
import db_controller

app = Flask(__name__)
db = db_controller.DbController()


@app.route('/getPersons', methods=['GET'])
def get_persons():
    persons = db.get_persons()
    response = jsonify({'persons': persons})
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.content_type = 'application/json'
    response.status = 200
    return response


@app.route('/addPerson')
def add_person():
    response = Response(status=200)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.content_type = 'application/json'
    return response


if __name__ == '__main__':
    app.run(debug=True)
