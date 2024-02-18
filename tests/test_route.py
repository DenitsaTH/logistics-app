from models.route import Route
from models.package import Package
from models.truck import Truck
from datetime import datetime, timedelta, time
import unittest

DEFAULT_DEPARTURE_DATETIME = datetime.combine(datetime.today() + timedelta(1), time(hour=6))
VALID_ID = 1
VALID_DISTANCES = [909, 877]
VALID_TIMEDELTA = 0
VALID_TRUCK = Truck(1, 'Scania', 42000, 8000)
VALID_CAPACITY_PER_STOP = []
VALID_STOPS = ['BRI', 'SYD', 'MEL']

route = Route(VALID_ID, VALID_DISTANCES, VALID_TIMEDELTA, DEFAULT_DEPARTURE_DATETIME, VALID_TRUCK,
              VALID_CAPACITY_PER_STOP, VALID_STOPS)


class Route_Should(unittest.TestCase):
    def test_initializerWithCorrectInput(self):
        self.assertEqual(VALID_ID, route.id)
        self.assertEqual(VALID_DISTANCES, route.distances)
        self.assertEqual(DEFAULT_DEPARTURE_DATETIME, route.departure_time)
        self.assertEqual(VALID_TRUCK, route.truck)
        self.assertEqual(VALID_CAPACITY_PER_STOP, route.delivery_weight_per_stop)
        self.assertEqual(VALID_STOPS, route.stops)

    def test_totalDistancesProperty_returnZeroWhenSumEmptyList(self):
        self.assertEqual(sum(VALID_DISTANCES), route.total_distance)

    def test_arrivalTimeProperty_returnDefaultDepartureTimeAtSixOClockTommorow(self):
        time_to_travel_in_mins = int((route.total_distance / Route.DEFAULT_SPEED) * 60)
        result = route.departure_time + timedelta(minutes=time_to_travel_in_mins)

        self.assertEqual(str(result), str(route.arrival_time))
        self.assertEqual(result, route.arrival_time)

    def test_findArrivalTimesFunction_whenDefaultDepartureTime(self):
        result = route.find_arrival_times()

        self.assertIsInstance(result, list)
        self.assertIsInstance(result[0], datetime)
        self.assertEqual(result, route.find_arrival_times())

    def test_getArrivalTimeForStopFunction_whenParamsAreValid_(self):
        arrival_time_for_stop = route.get_arrival_time_for_stop('MEL')
        result_str = arrival_time_for_stop

        self.assertIsInstance(result_str, str)
        self.assertEqual(result_str, str(arrival_time_for_stop))

    def test_getCapacityFunction_whenEnoughRouteCapacity(self):
        self.assertEqual([41950, 41950, 41950], route.get_capacity('BRI', 'SYD', 50))

    def test_getCapacityFunction_returnNoneWhenNotEnoughRouteCapacity(self):
        self.assertEqual(None, route.get_capacity('BRI', 'MEL', 45000))

    def test_getNextStopFunction_whenParamsAreValid(self):
        result = route.get_next_stop('SYD')

        self.assertIsInstance(result, tuple)
        self.assertIsInstance(result[0], str)
        self.assertIsInstance(result[1], datetime)

    def test_getNextStopFunction_returnValueError_whenStartLocationIsNone(self):
        with self.assertRaises(ValueError):
            route.get_next_stop()

    def test_removeStopFunction(self):
        route.remove_stop()

        self.assertEqual([909], route.distances)
        self.assertEqual(['BRI', 'SYD'], route.stops)

    def test_findNextStopAndArrivalTimeFunction(self):
        slots = route.find_arrival_times()
        result = route.find_next_stop_and_arrival_time(datetime.now(), slots)

        self.assertIsInstance(result, tuple)
        self.assertIsInstance(result[0], str)
        self.assertIsInstance(result[1], datetime)


    def test_strMethod(self):
        self.assertEqual('ID: [1] ', str(route))
