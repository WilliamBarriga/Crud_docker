import time
from flask import Flask
from flask.globals import request
from flask.templating import render_template
from mydatabase.consultas import gets, posts, deletes, updates

app = Flask(__name__)

back = '''<div>
        <br><br>
        <a href="/"><button>back</button></a>
        </div>
        '''


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
        return f'{gets.consultaNombre(nombre)} {back}'

    @app.route('/form_user', methods=['POST'])
    def get_user():
        user = request.form['user']
        return f'{gets.consultaUser(user)} {back}'

    @app.route('/form_id', methods=['POST'])
    def get_id():
        id = request.form['id']
        return f'{gets.consultaId(id)} {back}'

    @app.route('/form_region', methods=['POST'])
    def get_region():
        region = request.form['region']
        return f'{gets.consultaRegion(region)} {back}'

    @app.route('/form_all', methods=['POST'])
    def get_all():
        return f'{gets.all()} {back}'


class posting():
    @app.route('/post', methods=['GET'])
    def add():
        return render_template('post.html')

    @app.route('/post', methods=['POST'])
    def show_add():
        name = request.form['user']
        user = request.form['username']
        region = request.form['region']

        return f'{posts.agregar(name, user, region)} {back}'


class updating():
    @app.route('/update', methods=['GET'])
    def update():
        return render_template('update.html')

    @app.route('/update_user', methods=['POST'])
    def update_user():
        id = request.form['id']
        user = request.form['user']
        return f'{updates.update_user(id, user)} {back}'

    @app.route('/update_name', methods=['POST'])
    def update_name():
        id = request.form['id']
        name = request.form['name']
        return f'{updates.update_name(id, name)} {back}'

    @app.route('/update_region', methods=['POST'])
    def update_region():
        id = request.form['id']
        region = request.form['region']
        return f'{updates.update_region(id, region)} {back}'

    @app.route('/update_all', methods=['POST'])
    def update_all():
        id = request.form['id']
        user = request.form['user']
        name = request.form['name']
        region = request.form['region']
        return f'{updates.update_all(id, user, name, region)} {back}'


class deleting():

    @app.route('/delete', methods=['GET'])
    def delete():
        return render_template('delete.html')

    @app.route('/delete_id', methods=['POST'])
    def show_delete_id():
        id = request.form['id']
        return f'{deletes.delete_id(id)} {back}'

    @app.route('/delete_user', methods=['POST'])
    def show_delete_user():
        user = request.form['user']
        return f'{deletes.delete_user(user)} {back}'


if __name__ == "__main__":
    time.sleep(5)
    app.run(host='0.0.0.0', port=5000, debug=True)
