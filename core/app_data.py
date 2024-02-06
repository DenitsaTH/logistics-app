from models.route import Route
from models.package import Package


class AppData:
    def __init__(self) -> None:
        self.pending_packages = []  # all packages that are pending (have not be loaded on a specific truck)
        self.routes: list[Route] = []  # all generated routes (they have trucks and the trucks have packages)

    def add_package(self, package: Package):
        self.pending_packages.append(package)

    def add_route(self, route: Route):
        self.routes.append(route)

    def assign_package_to_route(self, package_id: int):
        # find package by id in self.pending_packages
        package = self.get_package(package_id)
        # looks for such a route in self.routes (hint: slice notation)
        package_start_location = package.start_location
        package_end_location = package.end_location
        package_kg = package.weight
        route = self.find_suitable_route(package_start_location, package_end_location, package_kg)
        # checks it truck exists; checks truck capacity [42, 42, 42, 0]
        if route:
            route.truck.add_package(package)
            self.pending_packages.remove(package)
            return f'Package #{package_id} bound for {package_end_location}'

        return f'No suitable route for this package! The package is in pending mode!'
        # route.truck.appnend(package)
        # else: Raise Error

    def view_route_information(self):
        # [r.info() for r in self.routes]
        raise NotImplementedError

    def view_package_information(self):
        # new_line = '\n'
        return '\n'.join([str(p) for p in self.pending_packages])

    def view_truck_information(self):
        raise NotImplementedError

    def get_route(self, route_id: int):
        for route in self.routes:
            if route.id == route_id:
                return route

    def get_package_info(self, id):
        raise NotImplementedError

    def get_package(self, package_id: int):
        for package in self.pending_packages:
            if package.id == package_id:
                return package

    def find_suitable_route(self, start_location, end_location, package_kg):
        for route in self.routes:
            for i in range(len(route.stops)):
                if start_location == route.stops[i] and end_location in route.stops[i + 1:]:
                    if route.truck and route.truck.capacity >= package_kg:
                        return route
        return
