from core.logistics_facade import LogisticsFacade
from core.menu import Menu


logistics_facade = LogisticsFacade()
menu = Menu(logistics_facade)
print(menu.menu_str)
user_input = input('Type [0] to view the menu or choose a command: \n')


while user_input != 'exit':

    try:
        execution = menu.execute(user_input)
        print(execution)
        user_input = input('\nType [0] to view the menu or choose a command:  \n')

    except Exception as err:
        print(err.args[0])
        user_input = input('\nType [0] to view the menu or choose a command:  \n')

print('\nGood Bye!')
