# copyright (c) 2025 AnonymoxZ
# This file is part of the AnonymoxZ project, licensed under the GNU General Public License v3.0.
# See the LICENSE file in the project root for more information.
from modules_system import painel_client, tools


client_playing = True
while client_playing:
    tools.clear()
    painel_client.screen_register()
    com = tools.filter_input(input('> '))
    if com == '0':
        painel_client.end_session()
        break
    
