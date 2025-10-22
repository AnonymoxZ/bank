# copyright (c) 2025 AnonymoxZ
import sqlite3 as db
from modules_system import tools, validators as val
from modules_system import painel_client



# testing db...
'''
def show_users():
    try:
        with db.connect(tools.pathdb()) as con:
            cursor = con.cursor()
            users_tab = cursor.execute("SELECT * FROM users").fetchall()
            for u in users_tab:
                for i in u:
                    print(i)
    except db.OperationalError:
        print('No register recent')
        tools.wait(2)
'''
# balance inquiry
# tranfers between clients
# register all actions of client
