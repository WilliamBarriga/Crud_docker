import mysql.connector
import json
import time

time.sleep(5)
cnx = mysql.connector.connect(
    user='root', password='secret', host='db', database='docker')
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
            cursor.execute(
                f"INSERT INTO `docker`.`users` (`name`, `username`, `region`) VALUES ('{name}', '{user}', '{region}');")
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
            cursor.execute(
                f"DELETE FROM `docker`.`users` WHERE (`idusers` = '{id}');")
            cnx.commit()
            return f'el usuario {result} se a eliminado'
        except:
            return 'parece que el usuario no se encunetra'

    def delete_user(user):
        try:
            result = gets.consultaUser(user)
            cursor.execute(
                f"DELETE FROM `docker`.`users` WHERE (`username` = '{user}');")
            cnx.commit()
            return f'el usuario {result} se a eliminado'
        except:
            return 'parece que el usuario no se encuentra'


class updates():

    def update_name(id, name):
        try:
            result = gets.consultaId(id)
            cursor.execute(
                f"UPDATE `docker`.`users` SET `name` = '{name}' WHERE (`idusers` = '{id}');")
            cnx.commit()
            time.sleep(1)
            final_result = gets.consultaId(id)
            return f'el usuario {result} ahora es {final_result}'
        except:
            return 'parece que el usuario no se encuentra'

    def update_user(id, user):
        try:
            result = gets.consultaId(id)
            cursor.execute(
                f"UPDATE `docker`.`users` SET `username` = '{user}' WHERE (`idusers` = '{id}');")
            cnx.commit()
            time.sleep(1)
            final_result = gets.consultaId(id)
            return f'el usuario {result} ahora es {final_result}'
        except:
            return 'parece que el usuario no se encuentra'

    def update_region(id, region):
        try:
            result = gets.consultaId(id)
            cursor.execute(
                f"UPDATE `docker`.`users` SET `region` = '{region}' WHERE (`idusers` = '{id}');")
            cnx.commit()
            time.sleep(1)
            final_result = gets.consultaId(id)
            return f'el usuario {result} ahora es {final_result}'
        except:
            return 'parece que el usuario no se encuentra'

    def update_all(id, user, name, region):
        try:
            result = gets.consultaId(id)
            cursor.execute(
                f"UPDATE `docker`.`users` SET `name` = '{name}', `username` = '{user}', `region` = '{region}' WHERE (`idusers` = '{id}');")
            cnx.commit()
            time.sleep(1)
            final_result = gets.consultaId(id)
            return f'el usuario {result} ahora es {final_result}'
        except:
            return 'parece que el usuario no se encuentra'
