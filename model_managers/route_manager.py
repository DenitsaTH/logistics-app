from models.route import Route
from core.app_data import AppData
from models.truck import Truck


class RouteManager:
    id = 1

    DISTANCES = {
        'SYD': {'MEL': 877,
                'ADL': 1376,
                'ASP': 2762,
                'BRI': 909,
                'DAR': 3935,
                'PER': 4016},
        'MEL': {'SYD': 877,
                'ADL': 725,
                'ASP': 2255,
                'BRI': 1765,
                'DAR': 3752,
                'PER': 3509},
        'ADL': {'SYD': 1376,
                'MEL': 725,
                'ASP': 1530,
                'BRI': 1927,
                'DAR': 3752,
                'PER': 3509},
        'ASP': {'SYD': 2762,
                'MEL': 2255,
                'ADL': 1530,
                'BRI': 2993,
                'DAR': 1497,
                'PER': 2481},
        'BRI': {'SYD': 909,
                'MEL': 1765,
                'ADL': 1927,
                'ASP': 2993,
                'DAR': 3426,
                'PER': 4311},
        'DAR': {'SYD': 3935,
                'MEL': 3752,
                'ADL': 3027,
                'ASP': 1497,
                'BRI': 3426,
                'PER': 4025},
        'PER': {'SYD': 4016,
                'MEL': 3509,
                'ADL': 22785,
                'ASP': 2481,
                'BRI': 4311,
                'DAR': 4025}
    }

    @classmethod
    def increment_id(cls):
        cls.id += 1

    def __init__(self, app_data: AppData) -> None:
        self.app_data = app_data

    # stop = [SYD, MEL, BRI, ASP, ADL] MEL - BRI stop[1:]
    # distances =  [877, 1765]
    def generate_route(self, *stops):
        distances = []

        for i in range(len(stops) - 1):
            distances.append(RouteManager.DISTANCES[stops[i]][stops[i + 1]])

        self.app_data.add_route(Route(RouteManager.id, distances, *stops))
        RouteManager.increment_id


    def get_route_by_id(self, route_id):
        return self.app_data.get_route(route_id)


    def assign_truck(self, id):
        route = self.get_route_by_id(id)

        if route.truck is not None:
            raise ValueError('This route already has an assigned truck!')

        if route.total_distance <= 8000:
            truck = Truck('Scania', len(route.stops))
        elif 8000 < route.total_distance <= 10000:
            truck = Truck('Man')
        elif 10000 < route.total_distance <= 13000:
            truck = Truck('Actros')
        else:
            raise ValueError('No truck with such km range!')

        route.truck = truck
        return f'Truck assigned to route:\n{truck}'
