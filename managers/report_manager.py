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
                slots = route.find_arrival_times()
                next_stop, arrival_time, status = route.find_next_stop_and_arrival_time(datetime_now, slots)
                result += f'\n{str(route)}\n-- Next stop: {next_stop}\nArrival time: {arrival_time} --'

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
            return f'Package with ID [{package_id}] is in pending mode at {package.start_location} warehouse'
        
        route_id = package.connected_route
        route = self.app_data.get_route_by_id(route_id)
        location, time, status = route.get_next_stop(start_location=package.start_location)
        arrival_time = route.get_arrival_time_for_stop(package.end_location)

        if status == 'to be loaded':
            return f'Package to be loaded at {location} at {time}. Final stop: {package.end_location} at {arrival_time}'
        elif status == 'en route':
            return f'Package en route. Next stop: {location} at {time}. Final stop: {package.end_location} at {arrival_time}'
        return f'Package delivered at {package.end_location}'
        
