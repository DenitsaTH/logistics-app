from datetime import datetime, timedelta, time
from models.package import Package
from models.truck import Truck


def add_days_to_now(d):
    return datetime.combine(datetime.today() + timedelta(d + 1), time(hour=6))


class Route:
    DEFAULT_DEPARTURE_DATETIME = datetime.combine(datetime.today() + timedelta(1), time(hour=6))
    DEFAULT_SPEED = 87

    def __init__(self, id: int, distances: list, time_delta, departure_time, truck, capacity_per_stop, stops) -> None:

        self.id = id
        self.distances = distances 

        if departure_time:
            self.departure_time = departure_time
        else:
            if time_delta == 0: 
                self.departure_time = Route.DEFAULT_DEPARTURE_DATETIME 
            else:
                self.departure_time = add_days_to_now(time_delta)

        self.stops = stops 
        self.truck = truck
        self.delivery_weight_per_stop = capacity_per_stop


    @property
    def total_distance(self):
        return sum(self.distances)


    @property
    def arrival_time(self):
        time_to_travel_in_mins = int((self.total_distance / Route.DEFAULT_SPEED) * 60)
        return self.departure_time + timedelta(minutes=time_to_travel_in_mins)


    def find_arrival_times(self):
        time_slots = [self.departure_time]
        current_slot = self.departure_time

        for d in self.distances:
            total_time_per_distance_in_mins = int((d / Route.DEFAULT_SPEED) * 60)
            arrival_time = current_slot + timedelta(minutes=total_time_per_distance_in_mins)
            time_slots.append(arrival_time)
            current_slot = arrival_time

        return time_slots
    

    def get_arrival_time_for_stop(self, stop: str):
        for i in range(len(self.stops)):
            if self.stops[i] == stop:
                result = self.find_arrival_times()[i]
                return self.custom_strftime("%b {S} %H:%Mh", result)


    def get_capacity(self, start_location: str, end_location: str, package_kg):
        route_capacity = [self.truck.capacity] * len(self.stops)
        start_idx, end_idx = 0, 0
        enough_capacity = True

        for i in range(len(self.stops)):
            if self.stops[i] == start_location:
                start_idx = i
            if self.stops[i] == end_location:
                end_idx = i

        for i in range(start_idx, end_idx):
            if package_kg > route_capacity[i]:
                enough_capacity = False
                break

        if enough_capacity:
            route_capacity = [r - package_kg for r in route_capacity if r in route_capacity[start_idx:end_idx]]
            self.delivery_weight_per_stop = [
                package_kg if idx in range(start_idx, end_idx) else self.delivery_weight_per_stop[idx]
                for idx in range(len(self.delivery_weight_per_stop))
            ]
            return route_capacity
        return


    def get_next_stop(self, start_location=None):
        datetime_now = datetime.now()
        slots = self.find_arrival_times()

        start_location_index = self.stops.index(start_location)
        load_time = slots[start_location_index]
        if datetime_now < load_time:
            return start_location, slots[start_location_index]
        return self.find_next_stop_and_arrival_time(datetime_now, slots)


    def remove_stop(self):
        self.stops.pop()
        self.distances.pop()


    def custom_strftime(self, format_string, t):
        def suffix(d):
            if 11 <= d <= 13:
                return 'th'
            else:
                return {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')

        return t.strftime(format_string).replace('{S}', str(t.day) + suffix(t.day))


    def find_next_stop_and_arrival_time(self, datetime_now, slots):
        if datetime_now < slots[0]:
            return self.stops[0], slots[0]
        for i in range(len(slots) - 1, -1, -1):
            current_slot = slots[i]
            if current_slot < datetime_now:
                if i == len(slots) - 1:
                    return self.stops[i], slots[i]
                return self.stops[i + 1], slots[i + 1]


    def __str__(self) -> str:
        route_id = f'ID: [{self.id}] '
        result = [f'{x} ({self.custom_strftime("%b {S} %H:%Mh", y)} delivery weight: {str(z)}kg)' for x, y, z in
                  zip(self.stops, self.find_arrival_times(), self.delivery_weight_per_stop)]
        return route_id + ' → '.join(result)
