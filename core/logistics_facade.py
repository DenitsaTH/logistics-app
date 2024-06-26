from core.app_data import AppData
from managers.package_manager import PackageManager
from managers.route_manager import RouteManager
from managers.truck_manager import TruckManager
from managers.report_manager import ReportManager
from core.helpers import file_is_empty
from core.save_state import save_state
from core.load_state import load_state


class LogisticsFacade:
    def __init__(self):
        self.app_data = AppData()
        self.package_manager = PackageManager(self.app_data)
        self.route_manager = RouteManager(self.app_data)

        if file_is_empty('db/trucks.txt'):
            self.truck_manager = TruckManager(self.app_data, True)
        else:
            self.truck_manager = TruckManager(self.app_data, False)
            self.load_state()

        self.report_manager = ReportManager(self.app_data)


    def create_route(self, *stops, time_delta=0):
        return self.route_manager.generate_route_from_input(time_delta, *stops)


    def create_package(self, start_point, end_point, weight, *customer_info):
        return self.package_manager.log_package(start_point, end_point, weight, *customer_info)


    def assign_truck_to_route(self, route_id: int):
        return self.route_manager.assign_truck(route_id)


    def assign_package_to_route(self, package_id: int):
        return self.app_data.assign_package_to_route(package_id)


    def view_pending_packages_information(self):
        return self.report_manager.get_pending_packages_report()


    def view_route_information(self, rule):
        return self.report_manager.get_route_report(rule)


    def search_for_package_per_client_request(self, package_id):
        return self.report_manager.get_package_report(package_id)


    def bulk_assign(self, location: str):
        packages, end_locations = self.app_data.check_backlog_for_location(location)
        if not packages:
            return f"No backlog for {location.upper()} warehouse!"
          
        locations = [location] + end_locations 
        self.create_route(*locations)
        route = self.app_data.routes[-1]

        while True:
            try:
                self.assign_truck_to_route(route.id)
                break
            except ValueError:
                route.remove_stop()

        result = ''
        for p in packages:
            result += '\n' + self.assign_package_to_route(p.id)
        return result


    def save_state(self):
        save_state(self.app_data)
        

    def load_state(self):
        load_state(self.package_manager, self.truck_manager, self.route_manager, self.app_data)
