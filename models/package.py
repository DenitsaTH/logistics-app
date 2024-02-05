from models.customer import Customer


# !!!TODO ENCAPSULATE THE CODE!!!

class Package:
    next_id = 1

    def __init__(self, start_location, end_location, weight: float, contact_info: Customer):
        self.id = Package.next_id
        self.start_location = start_location
        self.end_location = end_location
        self.weight = weight
        self.contact_info = contact_info
        Package.next_id += 1

    def __str__(self):
        contact_info_str = str(self.contact_info).replace('\n', '\n    ')
        return f'---Package info: ---\n' \
               f'   #Package ID: {self.id}\n' \
               f'   #Package start location: {self.start_location}\n' \
               f'   #Package end location: {self.end_location}\n' \
               f'   #Package weight: {self.weight}\n' \
               f'   ---Contact info: ---\n' \
               f'      {contact_info_str}'
