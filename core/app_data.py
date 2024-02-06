from models.route import Route
from models.package import Package


class AppData:
    def __init__(self) -> None:
        self.pending_packages = [] # all packages that are pending (have not be loaded on a specific truck)
        self.routes: list[Route] = [] # all generated routes (they have trucks and the trucks have packages)


    def add_package(self, package: Package):
        self.pending_packages.append(package)


    def add_route(self, route: Route):
        self.routes.append(route)

    
    def find_suitable_route(self, package_id: int):
        # find package by id in self.pending_packages
        # looks for such a route in self.routes (hint: slice notation)
        # checks it truck exists; checks truck capacity [42, 42, 42, 0]
        # route.truck.appnend(package)
        # else: Raise Error
        raise NotImplementedError


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
    