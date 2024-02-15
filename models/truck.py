class Truck:
    def __init__(self, id: int, brand: str, capacity: int, km_range: int, taken_time_slots=None) -> None:
        self._id = id
        self._brand = brand
        self._capacity = capacity
        self._km_range = km_range
        self.taken_time_slots = {} if taken_time_slots is None else taken_time_slots
                                  

    @property
    def id(self):
        return self._id
    

    @property
    def brand(self):
        return self._brand
    

    @property
    def capacity(self):
        return self._capacity
    

    @property
    def km_range(self):
        return self._km_range
    

    def is_time_slot_taken(self, route_id, start_time, end_time):
        for k, v in self.taken_time_slots.items():
            if start_time <= v[0] <= end_time or start_time <= v[1] <= end_time:
                return True
        return False
    

    def update_truck_time_slot(self, route_id, start_time, end_time):
        self.taken_time_slots[route_id] = [start_time, end_time]
    

    def __str__(self):
        return f'Truck information:\n' \
               f'ID: {self._id}\n' \
               f'Brand: {self._brand}\n' \
               f'Capacity: {self._capacity:.2f}kg\n' \
               f'Max range: {self._km_range}km'
    