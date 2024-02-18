from core.app_data import AppData
from managers.report_manager import ReportManager
from models.route import Route
from models.truck import Truck
from datetime import datetime, timedelta, time
from models.package import Package
from models.customer import Customer
import unittest


class ReportManager_Should(unittest.TestCase):
    def test_initializer_whenAppDataAttributeIsValid(self):
        appdata = AppData()
        report_manager = ReportManager(appdata)
        self.assertIsInstance(report_manager.app_data, AppData)

    def test_initializer_whenAppDataAttribteIsNotValid(self):
        with self.assertRaises(ValueError):
            ReportManager('')

    def test_getRouteReport_whenStatusIsNotStarted(self):
        def_depart_time = datetime.combine(datetime.today() + timedelta(1), time(hour=6))

        truck = Truck(1, 'Scania', 42000, 8000)

        route = Route(1, [909, 877], 0, def_depart_time, truck, [], ['BRI', 'SYD', 'MEL'])

        route_slots = route.find_arrival_times()
        route_next_stop, route_arrival_time = route.find_next_stop_and_arrival_time(datetime.now(), route_slots)

        appdata = AppData()

        appdata.add_route(route)

        report_manager = ReportManager(appdata)

        result = report_manager.get_route_report('all')

        expected_str = f'\n{str(route)}\nStatus: not started\n-- Next stop: {route_next_stop}\nArrival time: {route_arrival_time} --'

        self.assertIsInstance(result, str)
        self.assertEqual(expected_str, result)

    def test_getRouteReport_whenStatusIsFinished(self):
        def_depart_time = datetime.combine(datetime.today() + timedelta(-1), time(hour=6))

        truck = Truck(1, 'Scania', 42000, 8000)

        route = Route(1, [909, 877], 0, def_depart_time, truck, [], ['BRI', 'SYD', 'MEL'])

        route_slots = route.find_arrival_times()
        route_next_stop, route_arrival_time = route.find_next_stop_and_arrival_time(datetime.now(), route_slots)

        appdata = AppData()

        appdata.add_route(route)

        report_manager = ReportManager(appdata)

        result = report_manager.get_route_report('all')

        expected_str = f'\n{str(route)}\nStatus: finished\n-- Next stop: {route_next_stop}\nArrival time: {route_arrival_time} --'

        self.assertIsInstance(result, str)
        self.assertEqual(expected_str, result)

    def test_getRouteReport_whenStatusIsEnRouteAndRuleIsInProgress(self):
        def_depart_time = datetime.combine(datetime.today() + timedelta(-0.5), time(hour=6))

        truck = Truck(1, 'Scania', 42000, 8000)

        route = Route(1, [909, 877], 0, def_depart_time, truck, [], ['BRI', 'SYD', 'MEL'])

        route_slots = route.find_arrival_times()
        route_next_stop, route_arrival_time = route.find_next_stop_and_arrival_time(datetime.now(), route_slots)

        appdata = AppData()

        appdata.add_route(route)

        report_manager = ReportManager(appdata)

        result = report_manager.get_route_report('in progress')

        expected_str = f'\n{str(route)}\nStatus: en route\n-- Next stop: {route_next_stop}\nArrival time: {route_arrival_time} --'

        self.assertIsInstance(result, str)
        self.assertEqual(expected_str, result)

    def test_getPendingPackagesReportFunction_whenPendingPackagesFound(self):
        appdata = AppData()
        report_manager = ReportManager(appdata)

        customer = Customer('test', 'testov', 'test@gmail.com')

        package = Package(1, 'BRI', 'SYD', 50, customer, is_assigned=None,
                          connected_route=None)

        appdata.add_package(package)

        result = report_manager.get_pending_packages_report()

        expected_str = '\n-- PENDING PACKAGES: --\n' + f'\n{package}' + '\n--------'

        self.assertEqual(expected_str, result)

        self.assertIsInstance(result, str)

    def test_getPendingPackagesReportFunction_whenNotPendingPackages(self):
        appdata = AppData()

        report_manager = ReportManager(appdata)

        result = report_manager.get_pending_packages_report()

        expected_str = '\n-- NO PENDING PACKAGES --\n'

        self.assertEqual(expected_str, result)

        self.assertIsInstance(result, str)

    def test_getPackageReport_whenParameterIdIsValidAndPackageIsInPendingMode(self):
        appdata = AppData()
        report_manager = ReportManager(appdata)

        customer = Customer('test', 'testov', 'test@gmail.com')

        package = Package(1, 'BRI', 'SYD', 50, customer, is_assigned=None,
                          connected_route=None)

        appdata.add_package(package)

        result = report_manager.get_package_report(1)

        expected_str = f'Package with ID [{package.id}] is in pending mode at {package.start_location} warehouse'

        self.assertEqual(expected_str, result)

        self.assertIsInstance(result, str)

    def test_getPackageReportFunction_whenPackageIdIsNotValid(self):
        appdata = AppData()
        report_manager = ReportManager(appdata)

        result = report_manager.get_package_report(0)

        expected_str = 'No package with such ID!'

        self.assertEqual(expected_str, result)

        self.assertIsInstance(result, str)

    def test_getPackageReportFunction_whenRouteIsValidAndPackageIsDelivered(self):
        appdata = AppData()
        report_manager = ReportManager(appdata)

        def_depart_time = datetime.combine(datetime.today() + timedelta(-0.5), time(hour=6))

        truck = Truck(1, 'Scania', 42000, 8000)

        route = Route(1, [909, 877], 0, def_depart_time, truck, [], ['BRI', 'SYD', 'MEL'])

        customer = Customer('test', 'testov', 'test@gmail.com')

        package = Package(1, 'BRI', 'SYD', 50, customer, is_assigned=True, connected_route=1)

        appdata.add_route(route)
        appdata.add_package(package)
        appdata.add_truck(truck)

        result = report_manager.get_package_report(1)
        expected_str = f'Package delivered at {package.end_location}'

        self.assertEqual(expected_str, result)
        self.assertIsInstance(result, str)

    def test_getPackageReportFunction_whenRouteIsValidAndPackageIsToBeLoaded(self):
        appdata = AppData()
        report_manager = ReportManager(appdata)

        def_depart_time = datetime.combine(datetime.today() + timedelta(1), time(hour=6))

        truck = Truck(1, 'Scania', 42000, 8000)

        route = Route(1, [909, 877], 0, def_depart_time, truck, [], ['BRI', 'SYD', 'MEL'])

        customer = Customer('test', 'testov', 'test@gmail.com')

        package = Package(1, 'BRI', 'SYD', 50, customer, is_assigned=True, connected_route=1)

        appdata.add_route(route)
        appdata.add_package(package)
        appdata.add_truck(truck)

        route_arrival_time = appdata.routes[0].get_arrival_time_for_stop(package.end_location)
        route_next_stop, route_time = route.get_next_stop(package.start_location)

        expected_str = f'Package to be loaded at {package.start_location} at {route_time}. Final stop: {package.end_location} at {route_arrival_time}'

        result = report_manager.get_package_report(1)

        self.assertEqual(expected_str, result)

        self.assertIsInstance(result, str)

    def test_getPackageReportFunction_whenRouteIsValidAndPackageEnRoute(self):
        appdata = AppData()
        report_manager = ReportManager(appdata)

        def_depart_time = datetime.combine(datetime.today() + timedelta(0), time(hour=6))

        truck = Truck(1, 'Scania', 42000, 8000)

        route = Route(1, [909, 877], 0, def_depart_time, truck, [], ['BRI', 'SYD', 'MEL'])

        customer = Customer('test', 'testov', 'test@gmail.com')

        package = Package(1, 'SYD', 'MEL', 50, customer, is_assigned=True, connected_route=1)

        appdata.add_route(route)
        appdata.add_package(package)
        appdata.add_truck(truck)

        route_arrival_time = appdata.routes[0].get_arrival_time_for_stop(package.end_location)

        route_next_stop, route_time = route.get_next_stop(package.start_location)

        expected_str = f'Package en route. Next stop: {route_next_stop} at {route_time}. Final stop: {package.end_location} at {route_arrival_time}'

        result = report_manager.get_package_report(1)

        self.assertEqual(expected_str, result)
        self.assertIsInstance(result, str)
