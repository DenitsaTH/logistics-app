from models.route import Route
from models.package import Package
from models.truck import Truck
from models.customer import Customer
from core.app_data import AppData
from datetime import datetime, timedelta
import unittest

customer_1 = Customer('Gosho', 'Goshev', 'gosho@abv.bg')
truck_1 = Truck(1, 'Scania', 42000, 8000)
route_1 = Route(1, [909, 877], 0, datetime.now(), truck_1, [], ['BRI', 'SYD', 'MEL'])
package_1 = Package(1, 'BRI', 'SYD', 50, customer_1, None, None)


class AppData_Should(unittest.TestCase):
    def test_properties_returnTuple(self):
        appdata = AppData()
        self.assertEqual(tuple, type(appdata.trucks))
        self.assertEqual(tuple, type(appdata.routes))
        self.assertEqual(tuple, type(appdata.packages))

    def test_addPackageFunction_whenParameterIsValid(self):
        appdata = AppData()
        appdata.add_package(package_1)

        added_package = appdata.packages[0]

        self.assertEqual(added_package, package_1)

    def test_addPackageFunction_raisesValueErrorWhenParameterIsNotInstanceOfPackage(self):
        appdata = AppData()
        with self.assertRaises(ValueError):
            package = 'hey'
            appdata.add_package(package)

    def test_addRouteFunction_whenParameterIsValid(self):
        appdata = AppData()
        appdata.add_route(route_1)

        added_route = appdata.routes[0]

        self.assertEqual(added_route, route_1)

    def test_addRouteFunction_raisesValueErrorWhenParameterIsNotInstanceOfPackage(self):
        appdata = AppData()
        with self.assertRaises(ValueError):
            route = 'hey'
            appdata.add_route(route)

    def test_addTruckFunction_whenParameterIsValid(self):
        appdata = AppData()
        appdata.add_truck(truck_1)

        added_truck = appdata.trucks[0]

        self.assertEqual(added_truck, truck_1)

    def test_addTruckFunction_raisesValueErrorWhenParameterIsNotInstanceOfPackage(self):
        with self.assertRaises(ValueError):
            appdata = AppData()
            truck = 'hey'
            appdata.add_truck(truck)

    def test_findSuitableTruckFunction_whenAllParametersAreValid(self):
        # add truck to appdata.trucks collection
        appdata = AppData()

        appdata.add_truck(truck_1)

        # find a suitable truck from appdata.trucks collection
        found_truck = appdata.find_suitable_truck(1, 2, datetime.now(), datetime.now() + timedelta(1))

        self.assertEqual(truck_1, found_truck)

    def test_findSuitableTruckFunction_raiseValueErrorWhenNotFoundSuitableTruck(self):
        # appdata.trucks collection is empty

        with self.assertRaises(ValueError):
            appdata = AppData()
            start_time = datetime.now()
            end_time = datetime.now() + timedelta(1)
            appdata.find_suitable_truck(1, 22, start_time, end_time)

    def test_assignPackageToRouteFunction_whenParameterIsValid(self):
        appdata = AppData()

        appdata.add_package(package_1)
        appdata.add_route(route_1)
        appdata.add_truck(truck_1)
        result_str = appdata.assign_package_to_route(1)

        self.assertEqual(True, package_1.is_assigned)
        self.assertEqual(result_str, appdata.assign_package_to_route(1))

    def test_assignPackageToRouteFunction_whenPackageIdIsNotvalid(self):
        appdata = AppData()

        invalid_id_assign_package = appdata.assign_package_to_route(-1)

        result_str = 'No package with such ID!'

        self.assertEqual(result_str, invalid_id_assign_package)

    def test_assignPackageToRouteFunction_whenRouteNotExist(self):
        appdata = AppData()

        appdata.add_package(package_1)

        result_str = 'No suitable route for package with ID [1]! The package is in pending mode!'

        self.assertEqual(result_str, appdata.assign_package_to_route(1))

    def test_getRouteByIdFunction_whenParameterIdIsValid(self):
        appdata = AppData()

        appdata.add_route(route_1)

        self.assertEqual(route_1, appdata.get_route_by_id(1))

    def test_getRouteByIdFunction_returnNonewhenParameterIdIsNotValid(self):
        appdata = AppData()

        appdata.add_route(route_1)

        self.assertEqual(None, appdata.get_route_by_id(-1))

    def test_getPackageByIdFunction_whenParameterIdIsValid(self):
        appdata = AppData()

        appdata.add_package(package_1)

        self.assertEqual(package_1, appdata.get_package_by_id(1))

    def test_getPackageByIdFunction_returnNonewhenParameterIdIsNotValid(self):
        appdata = AppData()

        appdata.add_package(package_1)

        self.assertEqual(None, appdata.get_package_by_id(-1))

    def test_findSuitableRouteFunction_whenAllParametersAreValid(self):
        appdata = AppData()

        appdata.add_route(route_1)

        suitable_route = appdata.find_suitable_route('BRI', 'MEL')

        self.assertEqual(route_1, suitable_route)

    def test_findSuitableRouteFunction_whenAllParametersAreNotValid(self):
        appdata = AppData()

        invalid_suitable_route = appdata.find_suitable_route('BRI', 'SYD')

        self.assertEqual(None, invalid_suitable_route)

    def test_getAllPendingPackagesEndLocationsFunction_whenParameterIsValid(self):
        appdata = AppData()

        appdata.add_package(package_1)

        package_end_location = appdata.get_all_pending_packages_end_locations(appdata.packages)

        self.assertEqual(['SYD'], package_end_location)

    def test_checkBacklogForLocationFunction_whenParameterIsValid(self):
        appdata = AppData()
        package = Package(1, 'BRI', 'SYD', 50, customer_1, None, None)
        package_2 = Package(2, 'BRI', 'SYD', 50, customer_1, None, None)
        package_3 = Package(3, 'BRI', 'MEL', 50, customer_1, None, None)
        package_4 = Package(4, 'BRI', 'MEL', 50, customer_1, None, None)

        appdata.add_package(package)
        appdata.add_package(package_2)
        appdata.add_package(package_3)
        appdata.add_package(package_4)

        self.assertEqual(([package, package_2, package_3, package_4], ['SYD', 'MEL']),
                         appdata.check_backlog_for_location('BRI'))

    def test_checkBacklogForLocationFunction_whenPackagesAreLessThanThree(self):
        appdata = AppData()

        package = Package(1, 'BRI', 'SYD', 50, customer_1, None, None)
        package_2 = Package(2, 'BRI', 'SYD', 50, customer_1, None, None)

        appdata.add_package(package)
        appdata.add_package(package_2)

        self.assertEqual((None, None), appdata.check_backlog_for_location('BRI'))
