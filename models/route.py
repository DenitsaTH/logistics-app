from datetime import datetime, timedelta, time


class Route:
    DEFAULT_DEPARTURE_DATETIME = datetime.combine(datetime.today() + timedelta(1), time(hour=6))
    DEFAULT_SPEED = 87

    def __init__(self, id: int, distances: list, departure_time=None, *stops) -> None:
        
        self.id = id
        self.distances = distances

        if departure_time is None:
            self.departure_time = Route.DEFAULT_DEPARTURE_DATETIME
        else:
            self.departure_time = departure_time
        
        self.stops = stops
        self.truck = None


    @property
    def total_distance(self):
        return sum(self.distances)
    

    @property
    def arrival_time(self):
        time_to_travel_in_mins = int((self.total_distance / Route.DEFAULT_SPEED) * 60)
        return self.departure_time + timedelta(minutes=time_to_travel_in_mins)
    

    def find_next_stop_arrival_time(self):
        time_slots = [self.departure_time]
        current_slot = self.departure_time

        for d in self.distances:
            total_time_per_distance_in_mins = int((d / Route.DEFAULT_SPEED) * 60)
            arrival_time = current_slot + timedelta(minutes=total_time_per_distance_in_mins)
            time_slots.append(arrival_time)
            current_slot = arrival_time

        return time_slots


    def custom_strftime(self, format_string, t):
        def suffix(d):
            if 11 <= d <= 13:
                return 'th'
            else:
                return {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')

        return t.strftime(format_string).replace('{S}', str(t.day) + suffix(t.day))
    

    def __str__(self) -> str:
        result = [f'{x} ({self.custom_strftime("%b {S} %H:%Mh", y)})' for x, y in zip(self.stops, self.find_next_stop_arrival_time())]
        return ' → '.join(result)
