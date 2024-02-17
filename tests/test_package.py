from models.package import Package
from models.customer import Customer
import unittest

VALID_ID = 1
VALID_START_LOCATION = 'BRI'
VALID_END_LOCATION = 'MEL'
VALID_WEIGHT = 45.5
VALID_CONTACT_INFO = Customer('Test', 'Test', 'test@test.com')
VALID_IS_ASSIGNED = True
VALID_CONNECTED_ROUTE = 1


class Package_Should(unittest.TestCase):
    def test_initializerWithCorrectInput(self):
        package = Package(VALID_ID, VALID_START_LOCATION, VALID_END_LOCATION, VALID_WEIGHT, VALID_CONTACT_INFO,
                          VALID_IS_ASSIGNED, VALID_CONNECTED_ROUTE)

        self.assertEqual(VALID_ID, package._id)
        self.assertEqual(VALID_START_LOCATION, package._start_location)
        self.assertEqual(VALID_END_LOCATION, package._end_location)
        self.assertEqual(VALID_WEIGHT, package._weight)

        self.assertEqual(VALID_CONTACT_INFO, package.contact_info)  # contact_info should be Customer object

        # check types of is_assigned and connected_route
        self.assertEqual(bool, type(package.is_assigned))  # is_assigned should be bool
        self.assertEqual(int, type(package.connected_route))  # connected_route should be int

        self.assertEqual(float, type(package.weight))  # check if type of weight is float

    def test_initializerWithIncorrectInput(self):
        # start_location should be exactly 3 symbols

        with self.assertRaises(ValueError):  # start_location is not exactly 3 symbols
            Package(VALID_ID, 'Test', VALID_END_LOCATION, VALID_WEIGHT, VALID_CONTACT_INFO,
                    VALID_IS_ASSIGNED, VALID_CONNECTED_ROUTE)
        # end_location should be exactly 3 symbols

        with self.assertRaises(ValueError):  # end_location is not exactly 3 symbols
            Package(VALID_ID, VALID_START_LOCATION, 'Test', VALID_WEIGHT, VALID_CONTACT_INFO,
                    VALID_IS_ASSIGNED, VALID_CONNECTED_ROUTE)
        # weight should be type float, from 0 to 42 000 kilograms
        with self.assertRaises(ValueError):  # weight is 43 000 kg
            Package(VALID_ID, VALID_START_LOCATION, VALID_END_LOCATION, 43000, VALID_CONTACT_INFO,
                    VALID_IS_ASSIGNED, VALID_CONNECTED_ROUTE)
        with self.assertRaises(ValueError):  # weight is 43 000 kg
            Package(VALID_ID, VALID_START_LOCATION, VALID_END_LOCATION, -500, VALID_CONTACT_INFO,
                    VALID_IS_ASSIGNED, VALID_CONNECTED_ROUTE)

    def test_properties_whenTryToChange(self):
        package = Package(VALID_ID, VALID_START_LOCATION, VALID_END_LOCATION, VALID_WEIGHT, VALID_CONTACT_INFO,
                          VALID_IS_ASSIGNED, VALID_CONNECTED_ROUTE)

        with self.assertRaises(AttributeError):
            package.id = 2
        with self.assertRaises(AttributeError):
            package.start_location = 'Mel'
        with self.assertRaises(AttributeError):
            package.end_location = 'Bri'
        with self.assertRaises(AttributeError):
            package.weight = 10.500

    def test_strMethod_whenCorrect(self):
        package = Package(VALID_ID, VALID_START_LOCATION, VALID_END_LOCATION, VALID_WEIGHT, VALID_CONTACT_INFO,
                          VALID_IS_ASSIGNED, VALID_CONNECTED_ROUTE)

        contact_info_str = str(package.contact_info).replace('\n', '\n    ')

        valid_str = f'---Package info: ---\n' \
                    f'   #Package ID: [1]\n' \
                    f'   #Package start location: BRI\n' \
                    f'   #Package end location: MEL\n' \
                    f'   #Package weight: 45.5kg\n' \
                    f'   ---Contact info: ---\n' \
                    f'      {contact_info_str}'

        self.assertEqual(valid_str, str(package))
