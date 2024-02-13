from core.app_data import AppData
from models.customer import Customer
from models.package import Package
from core.validation_helpers import ensure_valid_params_count


class PackageManager:
    id = 1

    @classmethod
    def increment_id(cls):
        cls.id += 1


    def __init__(self, app_data: AppData) -> None:
        self.app_data = app_data


    def log_package(self, start_point, end_point, weight, *customer_info, is_assigned=False, connected_route=None):
        ensure_valid_params_count(min_expected_count=3, max_expected=3, actual_params=len(customer_info))
        first_name, last_name, email = customer_info
        customer_info = Customer(first_name, last_name, email)
        is_assigned = False if not is_assigned or is_assigned == 'False' else True
        connected_route = None if not connected_route or connected_route == 'None' else int(connected_route)
        package = Package(PackageManager.id, start_point, end_point, weight, customer_info, is_assigned, connected_route)
        self.app_data.add_package(package)

        PackageManager.increment_id()

        return f"\nPackage successfully logged!\n{str(package)}"
    