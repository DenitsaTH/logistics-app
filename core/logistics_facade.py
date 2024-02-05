from core.app_data import AppData
from model_managers.package_manager import PackageManager
from model_managers.route_manager import RouteManager


class LogisticsFacade:
    def __init__(self):
        self.app_data = AppData()
        self.package_service = PackageManager(self.app_data) # manages Packages
        self.route_manager = RouteManager(self.app_data) # manages Routes


    # Example commands:
    def create_package(self):
        pass

    def create_route(self, *stops):
        self.route_manager.generate_route(*stops)

    def find_route(self):
        pass

    def assign_truck_to_route(self, route, truck):
        self.route_manager.assign_truck(route, truck)

    def assign_package_to_route(self):
        pass

    def view_package_information(self):
        pass

    def view_route_information(self):
        """Each route's stops, delivery weight and expected current stop"""

    def view_trucks_information(self):
        pass
