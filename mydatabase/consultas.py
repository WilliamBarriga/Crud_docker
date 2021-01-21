import mysql.connector
import json
import time

time.sleep(5)
cnx = mysql.connector.connect(user='root', password='secret', host='db', database='docker')
cursor = cnx.cursor()

class gets():
    def consultaNombre(nombre):
        cursor.execute(f'SELECT * FROM docker.users WHERE name="{nombre}";')
        result = cursor.fetchall()
        return json.dumps(result)

    def consultaUser(user):
        cursor.execute(f'SELECT * FROM docker.users WHERE username="{user}";')
        result = cursor.fetchone()
        return json.dumps(result)

    def consultaId(id):
        cursor.execute(f'SELECT * FROM docker.users WHERE idusers={int(id)};')
        result = cursor.fetchone()
        return json.dumps(result)

    def consultaRegion(region):
        cursor.execute(f'SELECT * FROM docker.users WHERE region="{region}";')
        result = cursor.fetchall()
        return json.dumps(result)

    def all():
        cursor.execute('SELECT * FROM docker.users')
        result = cursor.fetchall()
        return json.dumps(result)

class posts():
    def agregar(name, user, region):
        try:
            cursor.execute(f"INSERT INTO `docker`.`users` (`name`, `username`, `region`) VALUES ('{name}', '{user}', '{region}');")
            cnx.commit()
            time.sleep(1)
            result = gets.consultaUser(user)
            return result
        except:
            return 'puede que el nombre de usuario ya se encuentre en uso pruebe con uno nuevo'

    def actualizar():
        pass


class deletes():
    def delete_id(id):
        try:
            result = gets.consultaId(id)
            cursor.execute(f"DELETE FROM `docker`.`users` WHERE (`idusers` = '{id}');")
            cnx.commit()
            return f'el usuario {result} se a eliminado'
        except:
            return 'parece que el usuario no se encunetra'

    def delete_user(user):
        try:
            result = gets.consultaUser(user)
            cursor.execute(f"DELETE FROM `docker`.`users` WHERE (`username` = '{user}');")
            cnx.commit()
            return f'el usuario {result} se a eliminado'
        except:
            return 'parece que el usuario no se encuentra'

class updates():
    def update_id(id):
        pass

    def update_user(user):
        pass

    def update_name(name):
        pass

    def update_all(id, user, name):
        pass