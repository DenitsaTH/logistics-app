from models.customer import Customer


class Package:
    next_id = 1

    def __init__(self, start_location, end_location, weight, contact_info: Customer):
        self.id = Package.next_id
        self.start_location = start_location
        self.end_location = end_location
        self.weight = weight
        self.contact_info = contact_info
        Package.next_id += 1

    def __str__(self):
        return f'{self.start_location} - {self.end_location} - {self.weight} - {self.contact_info}'


params = input().split()
package_start_location = params[0]
package_end_location = params[1]
package_weight = float(params[2])
package_contact_info = Customer(params[3], params[4], params[5])
package = Package(package_start_location, package_end_location, package_weight, package_contact_info)
print(package)
