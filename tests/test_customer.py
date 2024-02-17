from models.customer import Customer
import unittest

VALID_FIRST_NAME = 'Test'
VALID_LAST_NAME = 'Test'
VALID_EMAIL = 'test@test.com'


class Customer_Should(unittest.TestCase):
    def test_initializerWithCorrectInput(self):
        customer = Customer(VALID_FIRST_NAME, VALID_LAST_NAME, VALID_EMAIL)
        self.assertEqual(VALID_FIRST_NAME, customer._first_name)
        self.assertEqual(VALID_LAST_NAME, customer._last_name)
        self.assertEqual(VALID_EMAIL, customer._email)

    def test_properties_whenTryToChange(self):
        customer = Customer(VALID_FIRST_NAME, VALID_LAST_NAME, VALID_EMAIL)

        with self.assertRaises(AttributeError):
            customer.first_name = 'Test'
        with self.assertRaises(AttributeError):
            customer.last_name = 'Test'
        with self.assertRaises(AttributeError):
            customer.email = 'Test@abv.bg'

    def test_initializerWithIncorrectInput(self):
        # first_name should be from 2 to 15 characters
        with self.assertRaises(ValueError):  # first_name less than 2 characters
            Customer('T', VALID_LAST_NAME, VALID_EMAIL)
        with self.assertRaises(ValueError):  # first_name more than 15 characters
            Customer('Testtesttesttesttest', VALID_LAST_NAME, VALID_EMAIL)
        # last_name should be from 2 to 15 characters
        with self.assertRaises(ValueError):  # last_name less than 2 characters
            Customer(VALID_FIRST_NAME, 'T', VALID_EMAIL)
        with self.assertRaises(ValueError):  # last_name more than 15 characters
            Customer(VALID_FIRST_NAME, 'Testtesttesttesttest', VALID_EMAIL)
        # email should be from 5 to 30 characters and should contain '@' and '.' symbols
        with self.assertRaises(ValueError):  # email less than 5 characters
            Customer(VALID_FIRST_NAME, VALID_LAST_NAME, '@.bg')
        with self.assertRaises(ValueError):  # email more than 30 characters
            Customer(VALID_FIRST_NAME, VALID_LAST_NAME, 'testtesttesttesttesttestesttest@.bg')
        with self.assertRaises(ValueError):  # email without '@' symbol
            Customer(VALID_FIRST_NAME, VALID_LAST_NAME, 'test.bg')
        with self.assertRaises(ValueError):  # email without '@. symbol
            Customer(VALID_FIRST_NAME, VALID_LAST_NAME, 'test@bg')

    def test_strMethod_whenCorrect(self):
        valid_str = f'#First Name: Test\n' \
                    f'  #Last Name: Test\n' \
                    f'  #Email: Test@abv.bg'

        customer = Customer('Test', 'Test', 'Test@abv.bg')

        self.assertEqual(valid_str, str(customer))
