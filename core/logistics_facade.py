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

        self.load_state()


    def create_route(self, *stops, time_delta=0):
        return self.route_manager.generate_route(time_delta, *stops)


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


    def get_route_by_stops(self, *locations):
        return self.app_data.get_route_by_stops(*locations)


    def bulk_assign(self, location: str):
        packages, end_locations = self.app_data.check_backlog_for_location(location)
        if not packages:
            return f"No backlog for {location.upper()} warehouse!"
          
        locations = [location] + end_locations 
        self.create_route(*locations)
        route = self.get_route_by_stops(*locations)

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
        for p in self.app_data.packages:
            with open('db/packages.txt', 'a') as txt_file:
                txt_file.write(f'{p.start_location} {p.end_location} {p.weight} {p.contact_info.first_name} {p.contact_info.last_name} {p.contact_info.email} {p.is_assigned} {p.connected_route}' + '\n')


    def load_state(self):
        with open('db/packages.txt') as txt_file:
            for line in txt_file.readlines():
                if line:
                    start_location, end_location, weight, *customer_info, is_assigned, connected_route = line.split()
                    self.package_manager.log_package(start_location, end_location, weight, *customer_info, is_assigned=is_assigned, connected_route=connected_route)
