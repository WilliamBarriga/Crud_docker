import time
from flask import Flask
from flask.globals import request
from flask.templating import render_template
from mydatabase.consultas import gets, posts, deletes

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

class buscar():
    @app.route('/form', methods=['GET'])
    def hello_world():
        return render_template('get.html')

    @app.route('/form_name', methods=['POST'])
    def get_name():
        nombre = request.form['nombre']
        return gets.consultaNombre(nombre)

    @app.route('/form_user', methods=['POST'])
    def get_user():
        user = request.form['user']
        return gets.consultaUser(user)

    @app.route('/form_id', methods=['POST'])
    def get_id():
        id = request.form['id']
        return gets.consultaId(id)

    @app.route('/form_region', methods=['POST'])
    def get_region():
        region = request.form['region']
        return gets.consultaRegion(region)

    @app.route('/form_all', methods=['POST'])
    def get_all():
        return gets.all()

@app.route('/post', methods=['GET'])
def add():
    return render_template('post.html')

@app.route('/post', methods=['POST'])
def show_add():
    name = request.form['user']
    user = request.form['username']
    region = request.form['region']

    return posts.agregar(name, user, region)

@app.route('/update', methods=['GET'])
def update():
    return render_template('update.html')

@app.route('/update', methods=['POST'])
def show_update():
    pass

@app.route('/delete', methods=['GET'])
def delete():
    return render_template('delete.html')

@app.route('/delete_id', methods=['POST'])
def show_delete_id():
    id = request.form['id']
    return deletes.delete_id(id)

@app.route('/delete_user', methods=['POST'])
def show_delete_user():
    user = request.form['user']
    return deletes.delete_user(user)

if __name__ == "__main__":
    time.sleep(5)
    app.run(host='0.0.0.0',port=5000, debug=True)