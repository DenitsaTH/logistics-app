from models.customer import Customer

class Package:
    def __init__(self, id, start_location, end_location, weight: float, contact_info: Customer, is_assigned, connected_route):
        self._id = id

        if len(start_location) != 3:
            raise ValueError('Start location must be precisely 3 letters!')
        self._start_location = start_location

        if len(end_location) != 3:
            raise ValueError('End location must be precisely 3 letters!')
        self._end_location = end_location
        
        if float(weight) > 42000:
            raise ValueError('Weight еxceeds maximum truck capacity!')
        if float(weight) <= 0:
            raise ValueError('Weight should be a positive number!')
        self._weight = float(weight)
        
        self.contact_info = contact_info
        self.is_assigned = is_assigned
        self.connected_route = connected_route

    @property
    def id(self):
        return self._id

    @property
    def start_location(self):
        return self._start_location

    @property
    def weight(self):
        return self._weight

    @property
    def end_location(self):
        return self._end_location


    def __str__(self):
        contact_info_str = str(self.contact_info).replace('\n', '\n    ')
        return f'---Package info: ---\n' \
               f'   #Package ID: [{self._id}]\n' \
               f'   #Package start location: {self._start_location}\n' \
               f'   #Package end location: {self._end_location}\n' \
               f'   #Package weight: {self._weight}kg\n' \
               f'   ---Contact info: ---\n' \
               f'      {contact_info_str}'
