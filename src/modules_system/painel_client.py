# screens terminal

def screen_register():
    header_title = 'WELCOME TO MATTRESS $'
    print(f'''
{(len(header_title)+len(header_title))*"="}
         {header_title}
{(len(header_title)+len(header_title))*"="}
\t[ 1 ] Register Account
\t[ 2 ] Login Account
\t[ 3 ] Exit
''')


def screen_client(name):
    name_client = f'WELCOME {str(name).capitalize()}!'
    BR = (len(name_client)+len(name_client))*"="
    print(f'''{BR}\n\t{name_client}\n{BR}
    ( 1 ) Deposit
    ( 2 ) Withdrawal
    ( 3 ) Transfer
''')

