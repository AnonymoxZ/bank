# copyright (c) 2025 AnonymoxZ
# authentication and login system
import sqlite3 as db
from modules_system import tools, validators as val



def login_client(cpf, password):
    logged = False
    if  not val.valcpf(cpf) or not val.valpassword(password):
        tools.clear()
        return (logged, None)
    else:
        with db.connect(tools.pathdb()) as con:
            cursor = con.cursor()
            try:
                logged = True
                user_name = cursor.execute('''
                    SELECT name FROM users WHERE cpf=? AND password=?
                    ''',(cpf, password)).fetchone()
                if logged:
                    tools.clear()
                    return (logged, user_name[0])
            except:
                print('No register in database. Make sure registered as client of Mattres.')

