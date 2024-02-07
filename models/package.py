from models.customer import Customer


# !!!TODO ENCAPSULATE THE CODE!!!

class Package:
    def __init__(self, id, start_location, end_location, weight: float, contact_info: Customer):
        self.id = id
        self.start_location = start_location
        self.end_location = end_location
        self.weight = weight
        self.contact_info = contact_info
        self.is_assigned = False


    def __str__(self):
        contact_info_str = str(self.contact_info).replace('\n', '\n    ')
        return f'---Package info: ---\n' \
               f'   #Package ID: [{self.id}]\n' \
               f'   #Package start location: {self.start_location}\n' \
               f'   #Package end location: {self.end_location}\n' \
               f'   #Package weight: {self.weight}kg\n' \
               f'   ---Contact info: ---\n' \
               f'      {contact_info_str}'
