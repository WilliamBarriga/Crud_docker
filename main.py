import mysql.connector
import time

# time.sleep(5)
#cnx = mysql.connector.connect(user='root', password='secret', host='db')
#cursor = cnx.cursor()


def menu():
    print('-'*50)
    print('''
    Crud_Docker
    1)crear usuario
    2)listar usuarios
    3)actualizar usuarios
    4)eliminar usuarios
    5)salir
    ''')
    decisicion = input(': ')
    return decisicion


def _crear_user():
    pass


if __name__ == "__main__":
    while True:
        usuario = menu()
        if usuario == '1':
            print(1)
            continue
        elif usuario == '2':
            print(2)
            continue
        elif usuario == '3':
            print(3)
            continue
        elif usuario == '4':
            print(4)
            continue
        elif usuario == '5':
            print('adios')
            break
        else:
            print('error')
            break
