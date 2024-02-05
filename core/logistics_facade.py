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
        # self.package_manager.create_package(start_point, end_point, weight, *customer_info)
        raise NotImplementedError


    def create_route(self, *stops):
        self.route_manager.generate_route(*stops)


    def assign_truck_to_route(self, route_id, truck_id):
        self.route_manager.assign_truck(route, truck)


    def assign_package_to_route(self):
        # self.route_manager.assign_package(Package)
        raise NotImplementedError


    def view_package_information(self):
        raise NotImplementedError


    def view_route_information(self):
        """Each route's stops, delivery weight and expected current stop"""
        raise NotImplementedError


    def view_trucks_information(self):
        raise NotImplementedError
    

    def search_for_package_per_client_request(self, package_id):
        self.app_data.get_package_info(package_id)
