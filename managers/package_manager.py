from core.app_data import AppData
from models.customer import Customer
from models.package import Package
from core.validation_helpers import check_params_count


class PackageManager:
    id = 1

    @classmethod
    def increment_id(cls):
        cls.id += 1


    def __init__(self, app_data: AppData) -> None:
        self.app_data = app_data


    def log_package(self, start_point, end_point, weight, *customer_info):
        check_params_count(3, len(customer_info), 'customer info')
        customer_info = Customer(*customer_info)
        package = Package(PackageManager.id, start_point, end_point, weight, customer_info)
        self.app_data.add_package(package)

        PackageManager.increment_id()

        return f"Package successfully logged!\n{str(package)}"
    