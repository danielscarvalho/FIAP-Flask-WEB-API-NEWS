from flask import Flask, request, jsonify
import news_model as nm

# Na linha de comando execute:  flask --app news_service run
app = Flask(__name__)

@app.route('/', methods=['GET'])
def db_info():
    return jsonify(nm.get_db_info())

@app.route('/news/<id>', methods=['GET'])
def news_read(id):
    news = {"id":id}
    return jsonify(nm.read(news))

@app.route('/news/', methods=['POST'])
def news_create():
    news = request.get_json()
    return jsonify(nm.create(news))

@app.route('/news/<id>', methods=['PUT'])
def news_update(id):
    news = request.get_json()
    return jsonify(nm.update(news))

@app.route('/news/<id>', methods=['DELETE'])
def news_delete(id):
    news = {"id":id}
    return jsonify(nm.delete(news))