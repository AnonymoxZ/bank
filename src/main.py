# copyright (c) 2025 AnonymoxZ
# This file is part of the AnonymoxZ project, licensed under the GNU General Public License v3.0.
# See the LICENSE file in the project root for more information.
from modules_system import painel_client, tools
import client_register as cr
import custom_services as cs
import auth_login as log_in


# interfaces on
register_on = True
client_on = False
program_on = True
# ***************#


while program_on:
    tools.clear()
    if register_on:
        painel_client.screen_register()
        com = tools.filter_input(input('> '))
        match com:
            case '0':
                painel_client.end_session()
                break
            case '1':
                name_register = input('Enter your name: ')
                cpf_register = input('Enter your CPF: ')
                password_register = input('Enter an password(8 characters): ')
                cr.register(name_register, cpf_register, password_register)
            case '2':
                cpf_client = input('Enter with CPF: ')
                password_client = input('Enter with password: ')
                client_logged = log_in.login_client(cpf_client, password_client)
                if client_logged[0]:
                    client_on = True
                    register_on = False
                else:
                    print(tools.br, 'Not log in!' ,tools.br)
                    tools.wait()
                    continue
            case _:
                tools.clear()
                # ^_^

    elif client_on:
        painel_client.screen_client(client_logged[0], client_logged[1])
        com = tools.filter_input(input('> '))
        match com:
            case '0':
                tools.clear()
                print('Exit...')
                tools.wait(4)
                client_on = False
                register_on = True
            case _:
                tools.clear()

