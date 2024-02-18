from models.route import Route
from models.truck import Truck
from core.app_data import AppData
from managers.route_manager import RouteManager
from datetime import datetime, timedelta, time
import unittest


class RouteManager_Should(unittest.TestCase):
    def test_initializer_checkIsInstanceOfAppData(self):
        appdata = AppData()

        route_manager = RouteManager(appdata)

        self.assertIsInstance(route_manager.app_data, AppData)

    def test_initializer_raiseValueErrorWhenInvalidAttributeOfAppData(self):
        with self.assertRaises(ValueError):
            route_manager = RouteManager('k')

    def test_generateRouteFromInputFunction_whenParametersAreValid(self):
        # appdata.routes collection is empty now
        appdata = AppData()
        route_manager = RouteManager(appdata)

        # generate route and append the generated route to appdata.routes
        generated_route = route_manager.generate_route_from_input(0, 'BRI', 'SYD', 'MEL')

        # check if appdata.routes collection now has 1 element after calling of function generate_route_from_input
        self.assertEqual(len(appdata.routes), 1)

        route = appdata.routes[0]

        result_str = f'Below route with ID [{route.id}] successfully added:\n{str(route)}'

        self.assertEqual(result_str, generated_route)

    def test_generateRouteFromInputFunction_raiseValueErrorWhenParametersAreNotValid(self):
        appdata = AppData()
        route_manager = RouteManager(appdata)

        with self.assertRaises(ValueError):
            route_manager.generate_route_from_input(0, 0)

    def test_assignTruckFunction_whenIdParameterIsValid(self):
        appdata = AppData()
        route_manager = RouteManager(appdata)

        route_manager.generate_route_from_input(0, 'BRI', 'SYD')

        route = appdata.routes[0]

        truck = Truck(1, 'Scania', 42000, 8000)

        appdata.add_truck(truck)

        result_str = f'Truck with ID: [{appdata.trucks[0].id}] assigned to route with ID: [{appdata.routes[0].id}]!'

        self.assertEqual(result_str, route_manager.assign_truck(1))

        self.assertEqual(route.truck, truck)

    def test_assignTruckFunction_raisesValueErrorWhenRouteDoesNotExist(self):
        appdata = AppData()
        route_manager = RouteManager(appdata)
        with self.assertRaises(ValueError):
            route_manager.assign_truck(5)

    def test_assignTruckFunction_raisesValueErrorWhenTruckIsAlreadyAssigned(self):
        appdata = AppData()
        route_manager = RouteManager(appdata)

        truck = Truck(1, 'Scania', 42000, 8000)

        route = Route(1, [909, 877], 0, datetime.now(), None, [], ['BRI', 'SYD', 'MEL'])

        appdata.add_truck(truck)
        appdata.add_route(route)

        route_manager.assign_truck(1)

        with self.assertRaises(ValueError):
            route_manager.assign_truck(1)
