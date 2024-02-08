from models.route import Route
from core.app_data import AppData


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

    
    def generate_route(self, *stops):
        distances = []  # distances =  [877, 1765]

        for i in range(len(stops) - 1):
            distances.append(RouteManager.DISTANCES[stops[i]][stops[i + 1]])

        route = Route(RouteManager.id, distances, None, *stops)
        self.app_data.add_route(route)
        RouteManager.increment_id
        return f'Below route successfully added:\n{str(route)}'


    def get_route_by_id(self, route_id):
        return self.app_data.get_route_by_id(route_id)


    def assign_truck(self, id):
        route = self.get_route_by_id(id)

        if route.truck is not None:
            raise ValueError('This route already has an assigned truck!')
        
        total_distance = route.total_distance
        departure_time = route.departure_time
        arrival_time = route.arrival_time
        
        truck = self.app_data.find_suitable_truck(route.id, total_distance, departure_time, arrival_time)
        route.truck = truck

        return f'Truck with ID: [{truck.id}] assigned to route with ID: [{route.id}]!'
