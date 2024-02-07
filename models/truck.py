class Truck:
    def __init__(self, id: int, brand: str, capacity: int, km_range: int) -> None:
        self._id = id
        self._brand = brand
        self._capacity = capacity
        self._km_range = km_range
        self._taken_time_slots = {}


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
    

    @property
    def taken_time_slots(self):
        return self._taken_time_slots
    

    def is_time_slot_taken(self, route_id, start_time, end_time):
        for k, v in self.taken_time_slots.items():
            if start_time <= k[0] <= end_time or start_time <= k[1] <= end_time:
                return True
            self.taken_time_slots[route_id] = [start_time, end_time]
            return False


    def __str__(self):
        return f'Truck information:\n' \
               f'ID: {self._id}\n' \
               f'Brand: {self._brand}\n' \
               f'Capacity: {self._capacity:.2f}kg\n' \
               f'Max range: {self._km_range}km'
    