import io
from core.logistics_facade import LogisticsFacade
from core.menu import Menu


# file_path = 'use_cases/use_case4.txt'
logistics_facade = LogisticsFacade()
menu = Menu(logistics_facade)
# with open(file_path, 'r') as file:
#     user_input = input()
menu_str = '*_*_*_* MENU *_*_*_*\n' \
           'Type 0 for showing the menu\n' \
           'Type 1 for creating a route\n' \
           'Type 2 for assigning a truck to route\n' \
           'Type 3 for creating a package\n' \
           'Type 4 for assigning a package to route\n' \
           'Type 5 for bulk assign\n' \
           'Type 6 for searching_for a package per client request\n' \
           'Type 7 for view pending packages information\n' \
           'Type 8 for view route information\n' \
            'Type "exit" for exit the program\n' \
           '*_*_*_* MENU *_*_*_*\n'

print(menu_str)

user_input = input('Type 0 for showing menu or choose command: \n')

while user_input != 'exit':
    try:
        execution = menu.execute(user_input)
        print(execution)
        user_input = input('\nType 0 for showing menu or choose command: \n')

    except Exception as err:
        print(err.args[0])

        user_input = input('\nType 0 for showing menu or choose command: \n')
print('\nGood Bye!')
# print('\n'.join(output))
