from models.route import Route


class AppData:
    def __init__(self) -> None:
        self.pending_packages = [] # all packages that are pending (have not be loaded on a specific truck)
        self.routes = [] # all generated routes (they have trucks and the trucks have packages)


    def add_package(self, package: Package):
        # self.pending_packages.append(package)
        raise NotImplementedError


    def add_route(self, route: Route):
        self.routes.append(route)

    
    def find_suitable_route(self, start, end, weight):
        # looks for such a route in self.routes
        # if it exists - route.truck.appnend(package)
        # else: Raise Error
        raise NotImplementedError


    def view_route_information(self):
        # [r.info() for r in self.routes]
        raise NotImplementedError
    

    def view_package_information(self):
        raise NotImplementedError
    

    def view_truck_information(self):
        raise NotImplementedError


    def get_route(self, route_id):
        for route in self.routes:
            if route.id == route_id:
                return route
            

    def get_package_info(self, id):
        raise NotImplementedError
    