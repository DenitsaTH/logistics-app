from models.truck import Truck
import unittest


VALID_ID = 1
VALID_BRAND = 'Scania'
VALID_CAPACITY = 42000
VALID_KM_RANGE = 8000
VALID_TAKEN_TIME_SLOTS = None


class Truck_Should(unittest.TestCase):
    def test_initializerWithCorrectInput(self):
        truck = Truck(VALID_ID, VALID_BRAND, VALID_CAPACITY, VALID_KM_RANGE, VALID_TAKEN_TIME_SLOTS)

        self.assertEqual(VALID_ID, truck.id)
        self.assertEqual(VALID_BRAND, truck.brand)
        self.assertEqual(VALID_CAPACITY, truck.capacity)
        self.assertEqual(VALID_KM_RANGE, truck.km_range)

        self.assertEqual({}, truck.taken_time_slots)

    def test_properties_whenTryToChange(self):
        truck = Truck(VALID_ID, VALID_BRAND, VALID_CAPACITY, VALID_KM_RANGE, VALID_TAKEN_TIME_SLOTS)

        with self.assertRaises(AttributeError):
            truck.id = 2
            truck.brand = 'Test'
            truck.capacity = 45
            truck.km_range = 3000

    def test_strMethod_whenCorrect(self):
        truck = Truck(VALID_ID, VALID_BRAND, VALID_CAPACITY, VALID_KM_RANGE, VALID_TAKEN_TIME_SLOTS)
        valid_str = f'Truck information:\n' \
                    f'ID: 1\n' \
                    f'Brand: Scania\n' \
                    f'Capacity: 42000.00kg\n' \
                    f'Max range: 8000km'

        self.assertEqual(valid_str, str(truck))

    def test_is_time_slot_taken_returnFalseWhenTakenTimeSlotsAttributeIsNone(self):
        truck = Truck(VALID_ID, VALID_BRAND, VALID_CAPACITY, VALID_KM_RANGE, VALID_TAKEN_TIME_SLOTS)

        func = truck.is_time_slot_taken(1, 4, 5)

        self.assertEqual(False, func)
