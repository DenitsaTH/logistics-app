from core.logistics_facade import LogisticsFacade


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
                   '\nTO VIEW INFORMATION FOR ALL ROUTES IN PROGRESS, TYPE [8]\n' \
                   '\nTO EXIT THE PROGRAM, TYPE [Exit]\n' \
                   '\n*_*_*_* MENU *_*_*_*\n'


    def execute(self, user_input):
        cmd = user_input

        if cmd == '0':
            return self.menu_str


        if cmd == '1':
            print('To create a route, please enter <route stops> or type <back> to return to the main menu')

            stops = input('Route stops:\n').upper().split()

            if ''.join(stops).lower() == 'back':
                return 'Back to main menu!'

            time_delta = input(
                'Default departure time:\nTomorrow at 6:00\nTo choose another departure day, please enter a <number of days ahead> or <0> for default:\n')

            if len(stops) < 2:
                raise ValueError('Invalid input!')

            if time_delta == '0':
                return self.logistic_facade.create_route(*stops)
            return self.logistic_facade.create_route(*stops, time_delta=int(time_delta))


        if cmd == '2':
            print('To assign a truck to route, please enter <route ID> or type <back> to return to the main menu:')

            route_id = input('Route id:\n')

            if route_id == 'back':
                return 'Back to main menu!'

            if len(route_id) != 1:
                raise ValueError('Invalid input!')
            return self.logistic_facade.assign_truck_to_route(int(route_id))


        if cmd == '3':
            print(
                'To create a package, please enter:\n<start location>, <end location>, <weight>, <first name>, <last name>, <email> (separated by spaces)\nor type <back> to return to the main menu:\n')

            input_line = input('Package details: \n').split()

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
                'To assign a package to route, please enter <package ID> or type <back> to return to the main menu: \n')

            package_id = input('Package id: \n')

            if package_id.lower() == 'back':
                return 'Back to main menu!'
            
            return self.logistic_facade.assign_package_to_route(int(package_id))


        if cmd == '5':
            print('For bulk assign, please enter <warehouse name> or type <back> to return to the main menu: \n')
            warehouse_name = input('Warehouse name: \n').upper()

            if warehouse_name.lower() == 'back':
                return 'Back to main menu!'
            if len(warehouse_name) != 3:
                raise ValueError('Invalid input!')
            return self.logistic_facade.bulk_assign(warehouse_name)


        if cmd == '6':
            print(
                'To search for a package by ID, please enter <package ID> or type <back> to return to the main menu: \n')
            package_id = input('Package id: \n')

            if ''.join(package_id).lower() == 'back':
                return 'Back to main menu!'
            return self.logistic_facade.search_for_package_per_client_request(int(package_id))


        if cmd == '7':
            return self.logistic_facade.view_pending_packages_information()


        if cmd == '8':
            return self.logistic_facade.view_route_information()

        return 'Invalid command!'
