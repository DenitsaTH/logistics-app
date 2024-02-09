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
        for package in self.app_data.packages:
            if package.id == package_id:
                if not package.is_assigned:
                    return f'Package with id {package_id} is in pending mode!\nCurrent location: {package.start_location}'
                route_id = package.connected_route
                for route in self.app_data.routes:
                    if route.id == route_id:
                        if route.get_next_stop()[0] and route.get_next_stop()[1]:
                            return f'Package bound for {route.get_next_stop()[0]} at {route.get_next_stop()[1]} '
                        return f"Package waiting for load at {package.start_location}"
                    return f'Package delivered at {package.end_location}'
