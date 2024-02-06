from datetime import datetime, timedelta, time


class Route:
    DEFAULT_DEPARTURE_DATETIME = datetime.combine(datetime.today() + timedelta(1), time(hour=6))

    def __init__(self, id: int, distances: list, *stops) -> None:
        self.id = id 
        self.stops = list(stops)
        self.distances = distances
        self.departure_date_time = Route.DEFAULT_DEPARTURE_DATETIME
        self.truck = None


    @property
    def total_distance(self):
        return sum(self.distances)


    def __str__(self) -> str:
        """
        Brisbane (Oct 10th 06:00h) → Sydney (Oct 10th 20:00h) → Melbourne (Oct 11th 18:00h)
        Sydney (Oct 12th 06:00h) → Melbourne (Oct 12th 20:00h) → Adelaide (Oct 13th 15:00h) 
        """

        result = [(f'{x} ({self.custom_strftime('%b {S} %H:%Mh', y)})') for x, y in zip(self.stops, self.find_next_stop_arrival_time())]
        return ''.join(result)
    

    def find_next_stop_arrival_time(self):
        arrival_times = [self.departure_date_time]

        for d in self.distances:
            total_time_per_distance = d / 87 # self.truck.DEFAULT_SPEED
            arrival_time = self.DEFAULT_DEPARTURE_DATETIME + timedelta(total_time_per_distance)
            arrival_times.append(arrival_time)

        return arrival_times
    

    def custom_strftime(self, format_string, t):
        def suffix(d):
            if 11 <= d <= 13:
                return 'th'
            else:
                return {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')
        
        return t.strftime(format_string).replace('{S}', str(t.day) + suffix(t.day))
    