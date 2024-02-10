from core.logistics_facade import LogisticsFacade


class Menu:
    def __init__(self, logistic_facade: LogisticsFacade):
        self.logistic_facade = logistic_facade

    def execute(self, user_input):

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

        cmd = user_input

        if cmd == '0':
            return menu_str

        if cmd == '1':
            print('For creating a route, \n please enter ROUTE STOPS\n  or type "back" for back to main menu:\n ')

            input_line = input('Write: \n').upper().split()

            if ''.join(input_line).lower() == 'back':
                return 'Back to main menu!'

            time_delta = input(
                'Default departure time:\n Tomorrow at 6am\n To choose another day, please enter a number of days or keep 0 for default: \n')

            if len(input_line) < 2:
                raise ValueError('Invalid input!')

            if time_delta == '0':
                return self.logistic_facade.create_route(*input_line)  # ', '.join(input_line).upper()

            return self.logistic_facade.create_route(*input_line, time_delta=int(time_delta))

        if cmd == '2':
            print('For assigning truck to route, \n please enter ROUTE ID\n   or type "back" for back to main menu: ')

            input_line = input('Write: \n')

            if ''.join(input_line).lower() == 'back':
                return 'Back to main menu!'

            if len(input_line) != 1:
                raise ValueError('Invalid input!')

            return self.logistic_facade.assign_truck_to_route(int(input_line))

        if cmd == '3':
            print(
                'For creating a package, \n please enter\n  Start Location, End Location, Weight, First Name, Last Name, Email:\n   or type "back" for back to main menu:\n')

            input_line = input('Write: \n').split()

            if ''.join(input_line).lower() == 'back':
                return 'Back to main menu!'

            if len(input_line) < 6 or len(input_line) > 6:
                raise ValueError('Invalid input!')

            start_location = input_line[0].upper()
            end_location = input_line[1].upper()
            weight = input_line[2]
            contact_info = input_line[3:]

            return self.logistic_facade.create_package(start_location, end_location, float(weight), *contact_info)
        if cmd == '4':
            print(
                'For assigning a package to route,\n please enter\n  package ID\n   or type "back" for back to main menu: \n ')

            input_line = input('Write: \n')

            if ''.join(input_line).lower() == 'back':
                return 'Back to main menu!'

            if len(input_line) != 1:
                raise ValueError('Invalid input!')

            return self.logistic_facade.assign_package_to_route(int(input_line))

        if cmd == '5':
            print('For bulk assign,\n please enter\n  start location,\n   or type "back" for back to main menu: \n')
            input_line = input('Write: \n').upper()

            if ''.join(input_line).lower() == 'back':
                return 'Back to main menu!'
            if len(input_line) != 3:
                raise ValueError('Invalid input!')

            return self.logistic_facade.bulk_assign(input_line)

        if cmd == '6':
            print(
                'For searching_for a package per client request,\n please enter\n package ID,\n   or type "back" for back to main menu: \n')
            input_line = input('Write: \n')

            if ''.join(input_line).lower() == 'back':
                return 'Back to main menu!'
            if len(input_line) != 1:
                raise ValueError('Invalid input!')
            return self.logistic_facade.search_for_package_per_client_request(int(input_line))

        if cmd == '7':
            print('View pending packages information: \n')
            return self.logistic_facade.view_pending_packages_information()

        if cmd == '8':
            print('View route information: \n')
            return self.logistic_facade.view_route_information()

        return 'Invalid command!'
