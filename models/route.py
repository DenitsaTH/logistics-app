from datetime import *


class Route:
    DEFAULT_DEPARTURE_DATE = datetime.today() + timedelta(days=1)


    def __init__(self, id: int, distances: list, *stops) -> None:
        self.id = id 
        self.stops = list(stops)
        self.distances = distances
        self.departure_date = Route.DEFAULT_DEPARTURE_DATE


    def __str__(self) -> str:
        """
        Brisbane (Oct 10th 06:00h) → Sydney (Oct 10th 20:00h) → Melbourne (Oct 11th 18:00h)
        Sydney (Oct 12th 06:00h) → Melbourne (Oct 12th 20:00h) → Adelaide (Oct 13th 15:00h) 
        """
        return self.stops