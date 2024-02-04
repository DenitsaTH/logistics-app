from core.app_data import AppData
from model_services.package_service import PackageService
from model_services.route_manager import RouteManager


class LogisticsFacade:
    def __init__(self):
        app_data = AppData()
        package_service = PackageService(app_data) # manages Packages
        route_service = RouteManager(app_data) # manages Routes

    # Example commands:
        
    def add_package(self):
        pass

    def update_package(self):
        pass

    def create_route(self, *stops):
        self.route_manager.generate_route(*stops)

    def update_route(self):
        pass

    def view_route_information(self):
        pass

    def view_package_information(self):
        pass