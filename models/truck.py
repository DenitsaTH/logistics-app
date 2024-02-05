# TODO ENCAPSULATE
from models.package import Package
from models.customer import Customer


class Truck:
    trucks = {
        'Scania': {'next_id': 1001, 'end_id': 1010, 'capacity': 42000, 'max_range': 8000, 'number_of_vehicles': 10},
        'Man': {'next_id': 1011, 'end_id': 1025, 'capacity': 37000, 'max_range': 10000, 'number_of_vehicles': 15},
        'Actros': {'next_id': 1026, 'end_id': 1040, 'capacity': 26000, 'max_range': 13000, 'number_of_vehicles': 15}
    }

    def __init__(self, brand: str):
        self.brand = brand
        self.packages: list[Package] = []

        if self.trucks[brand]['number_of_vehicles'] > 0 and self.trucks[brand]['capacity'] > 0:

            self.truck_id = int(self.trucks[brand]['next_id'])
            self.capacity = float(self.trucks[brand]['capacity'])
            self.max_range = float(self.trucks[brand]['max_range'])
            self.number_of_vehicles = int(self.trucks[brand]['number_of_vehicles'])

            self.trucks[brand]['next_id'] += 1
            self.trucks[brand]['number_of_vehicles'] -= 1

            if self.truck_id > self.trucks[brand]['end_id']:
                raise ValueError(f'All IDs for truck brand "{brand}" have been allocated!')
        else:
            raise ValueError(f'No more trucks available for brand "{brand}".')

    def add_package(self, package: Package):
        if package not in self.packages:

            if package.weight > self.capacity:
                raise ValueError(f'Free capacity: {self.capacity}\nPackage weight: {package.weight:.2f}')
            self.packages.append(package)
            self.capacity -= package.weight

        else:
            raise ValueError('This package already exist!')

        return f'Package #{package.id} successfully added to the truck "{self.brand}" with ID: #{self.truck_id}'

    def find_package_by_id(self, package_id: int):
        for p in self.packages:
            if p.id == package_id:
                return p

        raise ValueError('This package has not been found!')

    def remove_package_by_id(self, package_id: int):
        package = []

        for p in self.packages:
            if p.id == package_id:
                package.append(p)
                self.capacity += p.weight

        if package:
            self.packages.remove(package[0])
        else:
            raise ValueError(f'Package with id "{package_id}" does not exist!')

        return f'Package #{package_id} is successfully removed from truck "{self.brand}" with ID: #{self.truck_id}'

    def __str__(self):
        return f'Truck with:\n' \
               f'ID: {self.truck_id}\n' \
               f'Brand: {self.brand}\n' \
               f'Capacity: {self.capacity}\n' \
               f'Max range: {self.max_range}'

# try:
#     contact = Customer('Pesho', 'Petrov', 'pesho@mail.bg')
#     pckg1 = Package('Varna', 'Sofia', 41000, contact)
#     pckg2 = Package('Sofia', 'Varna', 500, contact)
#     truck1 = Truck('Scania')
#     truck2 = Truck('Scania')
#
#     print(f'{truck1}\n\n{truck2}')
#     print()
#     print('----add package----')
#     print(truck1.add_package(pckg1))
#     print()
#     print('----add package-----')
#     print(truck1.add_package(pckg2))
#     print()
#     print(truck1)
#     print()
#     print('----find package by id----')
#     print(truck1.find_package_by_id(1))
#     print()
#     print('----remove package by id----')
#     print(truck1.remove_package_by_id(1))
#     print()
#     print(truck1)
#
#     truck1.add_package(pckg2)
# except Exception as err:
#     print('ERROR:')
#     print(err)
