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


    def generate_route_from_input(self, time_delta, *stops):
        distances = []

        for i in range(len(stops) - 1):
            distances.append(RouteManager.DISTANCES[stops[i]][stops[i + 1]])

        departure_time = None
        truck = None
        capacity_per_stop = [0] * len(stops)
        stops = [s for s in stops]

        route = Route(RouteManager.id, distances, time_delta, departure_time, truck, capacity_per_stop, stops)
        self.app_data.add_route(route)
        RouteManager.increment_id()
        return f'Below route with ID [{route.id}] successfully added:\n{str(route)}'
    

    def generate_route_from_file(self, distances, departure_time, stops, truck_id, delivery_weight_per_stop):
        distances = []

        for i in range(len(stops) - 1):
            distances.append(RouteManager.DISTANCES[stops[i]][stops[i + 1]])

        time_delta = None
        if truck_id != -1:
            truck = self.get_truck_by_id(truck_id)
        else:
            truck = None

        route = Route(RouteManager.id, distances, time_delta, departure_time, truck, delivery_weight_per_stop, stops)
        self.app_data.add_route(route)
        RouteManager.increment_id()


    def get_route_by_id(self, route_id):
        route = self.app_data.get_route_by_id(route_id)
        if route:
            return self.app_data.get_route_by_id(route_id)
        return
    

    def get_truck_by_id(self, truck_id):
        for t in self.app_data.trucks:
            if t.id == truck_id:
                return t


    def assign_truck(self, id):
        route = self.get_route_by_id(id)

        if route is None:
            raise ValueError('No route with such ID!')

        if route.truck is not None:
            raise ValueError('This route already has an assigned truck!')

        total_distance = route.total_distance
        departure_time = route.departure_time
        arrival_time = route.arrival_time

        truck = self.app_data.find_suitable_truck(route.id, total_distance, departure_time, arrival_time)
        route.truck = truck

        return f'Truck with ID: [{truck.id}] assigned to route with ID: [{route.id}]!'
