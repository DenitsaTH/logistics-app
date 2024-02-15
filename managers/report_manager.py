from core.app_data import AppData
from datetime import datetime


class ReportManager:
    def __init__(self, app_data: AppData):
        self.app_data = app_data


    def get_route_report(self, rule):
        datetime_now = datetime.now()
        result = ''
        for route in self.app_data.routes:
            slots = route.find_arrival_times()
            next_stop, arrival_time = route.find_next_stop_and_arrival_time(datetime_now, slots)
            if next_stop == route.stops[0]:
                status = 'not started'
            elif next_stop == route.stops[-1] and datetime_now > arrival_time:
                status = 'finished'
            else:
                status = 'en route'
            current_res_str = f'\n{str(route)}\nStatus: {status}\n-- Next stop: {next_stop}\nArrival time: {arrival_time} --'
            
            if rule == 'all':
                result += current_res_str
            if rule == 'in progress' and route.departure_time <= datetime_now <= route.arrival_time:
                result += current_res_str
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
        
        if not package:
            return f'No package with such ID!'
        if not package.is_assigned:
            return f'Package with ID [{package_id}] is in pending mode at {package.start_location} warehouse'
        
        route_id = package.connected_route
        route = self.app_data.get_route_by_id(route_id)
        next_stop, time = route.get_next_stop(start_location=package.start_location)
        arrival_time = route.get_arrival_time_for_stop(package.end_location)
        next_stop_index = route.stops.index(next_stop)
        package_start_location_index = route.stops.index(package.start_location)
        package_end_location_index = route.stops.index(package.end_location)

        if package_start_location_index >= next_stop_index:
            return f'Package to be loaded at {package.start_location} at {time}. Final stop: {package.end_location} at {arrival_time}'
        elif next_stop_index <= package_end_location_index:
            return f'Package en route. Next stop: {next_stop} at {time}. Final stop: {package.end_location} at {arrival_time}'
        return f'Package delivered at {package.end_location}'
        