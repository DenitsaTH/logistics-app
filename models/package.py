from models.customer import Customer

class Package:
    def __init__(self, id, start_location, end_location, weight: float, contact_info: Customer):
        self._id = id
        self._start_location = start_location
        self._end_location = end_location
        self._weight = weight
        self._contact_info = contact_info
        self._is_assigned = False
        self.connected_route = None

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
    def contact_info(self):
        return self._contact_info

    @property
    def end_location(self):
        return self._end_location

    @property
    def is_assigned(self):
        return self._is_assigned

    @is_assigned.setter
    def is_assigned(self, value):
        if value:
            self._is_assigned = value
        else:
            self._is_assigned = value

    # @property
    # def connected_route(self):
    #     return self._connected_route
    #
    # @connected_route.setter
    # def connected_route(self, value):
    #     if value:
    #         self._connected_route = value

    def __str__(self):
        contact_info_str = str(self.contact_info).replace('\n', '\n    ')
        return f'---Package info: ---\n' \
               f'   #Package ID: [{self.id}]\n' \
               f'   #Package start location: {self.start_location}\n' \
               f'   #Package end location: {self.end_location}\n' \
               f'   #Package weight: {self.weight}kg\n' \
               f'   ---Contact info: ---\n' \
               f'      {contact_info_str}'
