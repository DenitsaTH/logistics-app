from models.route import Route


class AppData:
    def __init__(self) -> None:
        self.pending_packages = [] # all packages that are pending (have not be loaded on a specific truck)
        self.routes = [] # all generated routes (they have trucks and the trucks have packages)


    def add_package(self, Package):
        pass


    def add_route(self, route: Route):
        self.routes.append(route)


    def view_route_information(self):
        # [r.info() for r in self.routes]
        pass