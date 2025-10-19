# copyright (c) 2025 AnonymoxZ
# this file register clients in db
import sqlite3 as db
from modules_system import validators as val, tools


def register(name, cpf, password):
    if (not val.valcpf(cpf)) and (not val.valpassword(password)):
        print('Invalid data! Check your CPF or make sure your password has 8 characters.')
    with db.connect(tools.pathdb()) as connect:
        cursor = connect.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            cpf TEXT UNIQUE,
            password TEXT);
        ''')
        try:
            cursor.execute('INSERT INTO users(name, cpf, password) VALUES (?,?,?)',
            (val.valname(name), cpf, password))
            print("Register with sucess!\n")
            print(cursor.execute("SELECT * FROM users;").fetchall())
            connect.commit()
        except db.IntegrityError:
            print(f'{tools.br}CPF has been register{tools.br}')

