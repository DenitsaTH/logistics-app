from core.app_data import AppData
from managers.package_manager import PackageManager
from managers.route_manager import RouteManager
from managers.truck_manager import TruckManager
from managers.report_manager import ReportManager


class LogisticsFacade:
    def __init__(self):
        self.app_data = AppData()
        self.package_manager = PackageManager(self.app_data)  
        self.route_manager = RouteManager(self.app_data)  
        self.truck_manager = TruckManager(self.app_data)  
        self.report_manager = ReportManager(self.app_data)  

    def create_route(self, *stops):
        return self.route_manager.generate_route(*stops)


    def create_package(self, start_point, end_point, weight, *customer_info):
        return self.package_manager.log_package(start_point, end_point, weight, *customer_info)


    def assign_truck_to_route(self, route_id: int):
        return self.route_manager.assign_truck(route_id)


    def assign_package_to_route(self, package_id: int):
        return self.app_data.assign_package_to_route(package_id)


    def view_all_packages_information(self):
        return self.report_manager.get_pending_packages_report()


    def view_route_information(self):
        return self.report_manager.get_route_report()


    def search_for_package_per_client_request(self, package_id):
        return self.report_manager.get_package_report(package_id)
