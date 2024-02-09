from core.app_data import AppData
from datetime import datetime


class ReportManager:
    def __init__(self, app_data: AppData):
        self.app_data = app_data


    def get_route_report(self):
        datetime_now = datetime.now()
        result = ''
        for route in self.app_data.routes:
            if route.departure_time <= datetime_now <= route.arrival_time:
                result += f'\n{str(route)}\n-- Next stop: {route.get_next_stop()[0]}\nArrival time: {route.get_next_stop()[1]} --'

        return result


    def get_pending_packages_report(self):
        result = ''
        for package in self.app_data.packages:
            if not package.is_assigned:
                result += f'\n{package}'

        if not result:
            return "\n-- NO PENDING PACKAGES --\n"
        
        return '\n-- PENDING PACKAGES: --\n' + result + '\n--------'


    def get_package_report(self, package_id: int):
        route_id = 0
        package = self.app_data.get_package_by_id(package_id)
        if not package.is_assigned:
            return f'Package with ID [{package_id}] is in pending mode!\nCurrent location: {package.start_location}'
        route_id = package.connected_route
        route = self.app_data.get_route_by_id(route_id)
        location, time = route.get_next_stop(end_location=package.end_location)
        
        if location == '':
            return f"Package waiting for load at {package.start_location}"
        elif location is None:
            return f'Package delivered at {package.end_location}'
        return f'Package bound for {package.end_location} at {time}'
