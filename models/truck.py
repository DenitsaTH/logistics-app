# TODO ENCAPSULATE
from models.package import Package


class Truck:
    trucks = {
        'Scania': {'next_id': 1001, 'end_id': 1010, 'capacity': 42000, 'max_range': 8000, 'number_of_vehicles': 10},
        'Man': {'next_id': 1011, 'end_id': 1025, 'capacity': 37000, 'max_range': 10000, 'number_of_vehicles': 15},
        'Actros': {'next_id': 1026, 'end_id': 1040, 'capacity': 26000, 'max_range': 13000, 'number_of_vehicles': 15}
    }

    def __init__(self, brand: str, stops_count: int):
        self.brand = brand
        self.packages: list[Package] = []

        if self.trucks[brand]['number_of_vehicles'] > 0:

            self.truck_id = int(Truck.trucks[brand]['next_id'])
            self.capacity = [float(Truck.trucks[brand]['capacity'])] * stops_count # [42000, 42000, 42000]
            # self.capacity = float(Truck.trucks[brand]['capacity']) 
            self.max_range = float(Truck.trucks[brand]['max_range'])

            Truck.trucks[brand]['next_id'] += 1
            Truck.trucks[brand]['number_of_vehicles'] -= 1

            if self.truck_id > Truck.trucks[brand]['end_id']:
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
               f'Capacity: {self.capacity}kg\n' \
               f'Max range: {self.max_range}km'
