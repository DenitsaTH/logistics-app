import unittest
import datetime
from core.logistics_facade import LogisticsFacade
from core.app_data import AppData
from managers.package_manager import PackageManager
from managers.route_manager import RouteManager
from managers.truck_manager import TruckManager
from managers.report_manager import ReportManager


class LogisticsFacade_Should(unittest.TestCase):
    def setUp(self) -> None:
        self.test_facade = LogisticsFacade()

    def test_initCreatesLogisticsFacade(self):
        self.assertIsInstance(self.test_facade, LogisticsFacade)
        self.assertIsInstance(self.test_facade.app_data, AppData)
        self.assertIsInstance(self.test_facade.package_manager, PackageManager)
        self.assertIsInstance(self.test_facade.route_manager, RouteManager)
        self.assertIsInstance(self.test_facade.truck_manager, TruckManager)
        self.assertIsInstance(self.test_facade.report_manager, ReportManager)

    def test_createRoute_returnsExpectedValue(self):
        actual_result = self.test_facade.create_route('SYD', 'BRI')
        route = self.test_facade.app_data.routes[-1]
        expected_result = f'Below route with ID [{route.id}] successfully added:\nID: [{route.id}] SYD ({route.custom_strftime("%b {S} %H:%Mh", route.departure_time)} delivery weight: 0kg) → BRI ({route.custom_strftime("%b {S} %H:%Mh", route.arrival_time)} delivery weight: 0kg)'
        self.assertEqual(expected_result, actual_result)

    def test_createPackage_returnsExpectedValue(self):
        actual_result = self.test_facade.create_package('BRI', 'SYD', 45, 'Georgi', 'Georgive', 'gosho@abv.bg')
        package = self.test_facade.app_data.packages[-1]
        contact_info_str = str(package.contact_info).replace('\n', '\n    ')
        expected_result = f'\nPackage successfully logged!\n---Package info: ---\n' \
               f'   #Package ID: [{package.id}]\n' \
               f'   #Package start location: {package.start_location}\n' \
               f'   #Package end location: {package.end_location}\n' \
               f'   #Package weight: {package.weight}kg\n' \
               f'   ---Contact info: ---\n' \
               f'      {contact_info_str}'
        self.assertEqual(expected_result, actual_result)

    def test_assignTruckToRoute_returnsExpectedValue(self):
        self.test_facade.create_route('SYD', 'BRI')
        route = self.test_facade.app_data.routes[-1]
        actual_result = self.test_facade.assign_truck_to_route(route.id)
        expected_result = f'Truck with ID: [1001] assigned to route with ID: [{route.id}]!'

        self.assertEqual(expected_result, actual_result)

    def test_assignTruckToRoute_raisesError_whenAlreadyAssigned(self):
        self.test_facade.create_route('SYD', 'BRI')
        route = self.test_facade.app_data.routes[-1]
        self.test_facade.assign_truck_to_route(route.id)

        with self.assertRaises(ValueError):
            self.test_facade.assign_truck_to_route(route.id)

    def test_assignTruckToRoute_raisesError_whenNoSuchRouteId(self):
        with self.assertRaises(ValueError):
            self.test_facade.assign_truck_to_route(-1)

    def test_assignPackage_returnsExpectedValue_whenNoSuchRoute(self):
        self.test_facade.create_package('BRI', 'SYD', 45, 'Georgi', 'Georgive', 'gosho@abv.bg')
        package = self.test_facade.app_data.packages[-1]

        actual_result = self.test_facade.assign_package_to_route(package.id)
        expected_result = f'No suitable route for package with ID [{package.id}]! The package is in pending mode!'
        self.assertEqual(expected_result, actual_result)

    def test_assignPackage_returnsExpectedValue_whenNoSuchPackage(self):
        actual_result = self.test_facade.assign_package_to_route(-1)
        expected_result = 'No package with such ID!'

        self.assertEqual(expected_result, actual_result)

    def test_assignPackage_returnsCorrectValue_whenAssigned(self):
        self.test_facade.create_package('BRI', 'SYD', 45, 'Georgi', 'Georgive', 'gosho@abv.bg')
        package = self.test_facade.app_data.packages[-1]
        self.test_facade.create_route('BRI', 'SYD')
        route = self.test_facade.app_data.routes[-1]
        self.test_facade.assign_truck_to_route(route.id)
        route = self.test_facade.app_data.routes[-1]
        arrival_time = route.arrival_time

        actual_result = self.test_facade.assign_package_to_route(package.id)
        expected_result = f'Package #{package.id} bound for {package.end_location}. Planned arrival time: {route.custom_strftime("%b {S} %H:%Mh", route.arrival_time)}'
        self.assertEqual(expected_result, actual_result)