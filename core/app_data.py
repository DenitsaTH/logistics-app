from models.route import Route
from models.package import Package
from models.truck import Truck


class AppData:
    def __init__(self) -> None:
        self._trucks: list[Truck] = [] 
        self._routes: list[Route] = []  
        self._packages: list[Package] = [] 

    @property
    def packages(self):
        return tuple(self._packages)
    

    @property
    def routes(self):
        return tuple(self._routes)
    

    @property
    def trucks(self):
        return tuple(self._trucks)


    def add_package(self, package: Package):
        return self._packages.append(package)


    def add_route(self, route: Route):
        return self._routes.append(route)


    def add_truck(self, truck: Truck):
        self._trucks.append(truck)


    def find_suitable_truck(self, route_id, distance: int, start_time, end_time):
        for truck in self._trucks:
            if truck.km_range >= distance and not truck.is_time_slot_taken(route_id, start_time, end_time):
                return truck
        raise ValueError("No available truck for this time slot!")


    def assign_package_to_route(self, package_id: int):
        package = self.get_package_by_id(package_id)

        package_start_location = package.start_location
        package_end_location = package.end_location
        package_kg = package.weight

        route = self.find_suitable_route(package_start_location, package_end_location, package_kg)

        if route:
            route.add_package(package)
            package.connected_route = route.id
            package.is_assigned = True
            if route.get_capacity(package_start_location, package_end_location, package_kg):
                return f'Package #{package_id} bound for {package_end_location}'

        return f'No suitable route for this package! The package is in pending mode!'


    def get_route_by_id(self, route_id: int):
        for route in self.routes:
            if route.id == route_id:
                return route
            

    def get_package_by_id(self, package_id: int):
        for package in self.packages:
            if package.id == package_id:
                return package


    def find_suitable_route(self, start_location, end_location, package_kg):
        for route in self.routes:
            for i in range(len(route.stops)):
                if start_location == route.stops[i] and end_location in route.stops[i + 1:]:
                    # index = route.stops.index(start_location)
                    if route.truck and route.truck.capacity >= package_kg:
                        return route
        return
