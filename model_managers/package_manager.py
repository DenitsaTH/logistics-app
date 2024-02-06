from core.app_data import AppData
from models.customer import Customer
from models.package import Package


class PackageManager:
    # creates a Customer using the customer info and passes it as a param to Package()
    
    id = 1

    @classmethod
    def increment_id(cls):
        cls.id += 1


    def __init__(self, app_data: AppData) -> None:
        self.app_data = app_data


    def log_package(self, start_point, end_point, weight, *customer_info):
        customer_info = Customer(*customer_info)
        package = Package(PackageManager.id, start_point, end_point, weight, customer_info)
        self.app_data.add_package(package)

        PackageManager.increment_id()

        return f"Package successfully logged! Package info:\n{str(package)}"

