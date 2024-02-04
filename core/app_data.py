from models.route import Route


class AppData:
    def __init__(self) -> None:
        self.pending_packages = [] # all packages that are pending (have not be loaded on a specific truck)
        self.routes = [] # all generated routes


    def add_package(self, Package):
        pass


    def add_route(self, route: Route):
        self.routes.append(route)