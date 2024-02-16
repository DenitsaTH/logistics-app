from core.logistics_facade import LogisticsFacade
from core.helpers import ensure_valid_params_count, check_if_valid_stops, parse_to_integer, check_if_valid_warehouse


class Menu:
    def __init__(self, logistic_facade: LogisticsFacade):
        self.logistic_facade = logistic_facade
        self.menu_str = '\n*_*_*_* MENU *_*_*_*\n' \
                   '\nTO VIEW THE MENU, TYPE [0]\n' \
                   '\nTO CREATE A ROUTE, TYPE [1]\n' \
                   '\nTO ASSIGN A TRUCK TO ROUTE, TYPE [2]\n' \
                   '\nTO CREATE A PACKAGE, TYPE [3]\n' \
                   '\nTO ASSIGN A PACKAGE TO ROUTE, TYPE [4]\n' \
                   '\nTO BULK ASSIGN, TYPE [5]\n' \
                   '\nTO SEARCH FOR A PACKAGE BY ID, TYPE [6]\n' \
                   '\nTO VIEW INFORMATION FOR ALL PENDING PACKAGES, TYPE [7]\n' \
                   '\nTO VIEW INFORMATION FOR ALL ROUTES, TYPE [8]\n' \
                   '\nTO EXIT THE PROGRAM, TYPE [Exit]\n' \
                   '\n*_*_*_* MENU *_*_*_*\n'


    def back_to_main_menu(self, input_str):
        input_string = ''.join(input_str).lower()
        if input_string == 'back':
            return True
        

    def execute(self, user_input):
        cmd = user_input

        if cmd == '0':
            return self.menu_str
        

        if cmd == '1':
            print('To create a route, please enter at least 2 <route stops> or type <back> to return to the main menu')
            stops = input('Route stops:\n').upper().split()
            if self.back_to_main_menu(stops):
                return 'Back to main menu!'
            
            if not ensure_valid_params_count(min_expected_count=2, actual_params=len(stops)):
                stops = input('At least 2 stops required!\n').upper().split()
            if self.back_to_main_menu(stops):
                return 'Back to main menu!'
            if not check_if_valid_stops(stops):
                stops = input('Invalid stop(s)! Please choose from the following: SYD, MEL, ADL, ASP, BRI, DAR, PER\n').upper().split()
            if self.back_to_main_menu(stops):
                return 'Back to main menu!'

            time_delta = input(
                'Default departure time:\nTomorrow at 6:00\nTo choose another departure day, please enter a <number of days ahead> or <0> for default:\n')
            if self.back_to_main_menu(time_delta):
                return 'Back to main menu!'
            time_delta = parse_to_integer(time_delta)

            while True:
                if not isinstance(time_delta, int):
                    time_delta = input('Enter a number for days ahead!\n')
                    if self.back_to_main_menu(time_delta):
                        return 'Back to main menu!'
                elif time_delta == 0:
                    return self.logistic_facade.create_route(*stops)
                return self.logistic_facade.create_route(*stops, time_delta=int(time_delta))


        if cmd == '2':
            print('To assign a truck to route, please enter <route ID> or type <back> to return to the main menu:')
            route_id = input('Route id:\n')
            if self.back_to_main_menu(route_id):
                return 'Back to main menu!'
        
            if not ensure_valid_params_count(max_expected=1, actual_params=len(route_id.split())):
                route_id = input('Please input only one ID!\n')
                if self.back_to_main_menu(route_id):
                    return 'Back to main menu!'
            
            integer_value = parse_to_integer(route_id)

            while True:
                if not isinstance(integer_value, int):
                    route_id = input("ID is not a valid number!\n")
                    if self.back_to_main_menu(route_id):
                        return 'Back to main menu!'
                return self.logistic_facade.assign_truck_to_route(int(route_id))


        if cmd == '3':
            print(
                'To create a package, please enter:\n<start location>, <end location>, <weight>, <first name>, <last name>, <email> (separated by spaces)\nor type <back> to return to the main menu:\n')
            input_line = input('Package details: \n').split()
            if self.back_to_main_menu(input_line):
                return 'Back to main menu!'

            if not ensure_valid_params_count(min_expected_count=6, max_expected=6, actual_params=len(input_line)):
                input_line = input('One of the required fields is missing or too many fields!\n').split()
                if self.back_to_main_menu(input_line):
                    return 'Back to main menu!'

            start_location = input_line[0].upper()
            end_location = input_line[1].upper()
            weight = input_line[2]
            contact_info = input_line[3:]
            return self.logistic_facade.create_package(start_location, end_location, float(weight), *contact_info)
        

        if cmd == '4':
            print(
                'To assign a package to route, please enter <package ID> or type <back> to return to the main menu: \n')
            package_id = input('Package id: \n')
            if self.back_to_main_menu(package_id):
                return 'Back to main menu!'

            if not ensure_valid_params_count(max_expected=1, actual_params=len(package_id)):
                package_id = input('Please input only one ID!\n')
                if self.back_to_main_menu(package_id):
                    return 'Back to main menu!'
            
            integer_value = parse_to_integer(package_id)
            
            while True:
                if not isinstance(integer_value, int):
                    package_id = input("ID is not a valid number!\n")
                    if self.back_to_main_menu(package_id):
                        return 'Back to main menu!'
                return self.logistic_facade.assign_package_to_route(int(package_id))


        if cmd == '5':
            print('For bulk assign, please enter <warehouse name> or type <back> to return to the main menu: \n')
            warehouse_name = input('Warehouse name: \n').upper()
            if self.back_to_main_menu(warehouse_name):
                return 'Back to main menu!'

            if not check_if_valid_warehouse(warehouse_name):
                warehouse_name = input('Invalid warehouse name! Please choose from the following: SYD, MEL, ADL, ASP, BRI, DAR, PER\n').upper().split()
                if self.back_to_main_menu(warehouse_name):
                    return 'Back to main menu!'
            return self.logistic_facade.bulk_assign(warehouse_name)


        if cmd == '6':
            print(
                'To search for a package by ID, please enter <package ID> or type <back> to return to the main menu: \n')
            package_id = input('Package id: \n')
            if self.back_to_main_menu(package_id):
                return 'Back to main menu!'

            integer_value = parse_to_integer(package_id)
            
            while True:
                if not isinstance(integer_value, int):
                    package_id = input("ID is not a valid number!\n")
                    if self.back_to_main_menu(package_id):
                        return 'Back to main menu!'
                return self.logistic_facade.search_for_package_per_client_request(int(package_id))


        if cmd == '7':
            return self.logistic_facade.view_pending_packages_information()


        if cmd == '8':
            input_line = input('Type <all> to view information for all routes or <in progress> to view information only for routes in progress\n')
            if self.back_to_main_menu(input_line):
                return 'Back to main menu!'
            
            if input_line == 'all':
                result = self.logistic_facade.view_route_information('all')
                if not result:
                    return 'No routes'
                return result
            result = self.logistic_facade.view_route_information('in progress')

            if not result:
                return 'No routes in progress'
            return result


        return 'Invalid command!'
