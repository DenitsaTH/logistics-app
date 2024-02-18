from models.truck import Truck
from core.app_data import AppData
from managers.truck_manager import TruckManager
import unittest


class TruckManager_Should(unittest.TestCase):
    def test_initializer_withClosedGarage(self):
        appdata = AppData()
        should_open_garage = False
        truck_manager = TruckManager(appdata, should_open_garage)

        self.assertEqual(appdata, truck_manager.app_data)
        self.assertEqual(should_open_garage, truck_manager.should_open_garage)
        self.assertIsInstance(appdata, AppData)
        self.assertIsInstance(should_open_garage, bool)

    def test_initializer_raiseValueErrorWhenParameterAppDataIsNotValid(self):
        with self.assertRaises(ValueError):
            TruckManager(0, False)

    def test_initializer_returnFalseWhenShouldOpenGarageAttributeIsNotBool(self):
        appdata = AppData()
        should_open_garage = ''
        truck_manager = TruckManager(appdata, should_open_garage)
        self.assertEqual(False, truck_manager.should_open_garage)

    def test_openGarageFunction_whenShouldOpenGarageAttributeIsTrue(self):
        appdata = AppData()
        should_open_garage = True
        truck_manager = TruckManager(appdata, should_open_garage)

        self.assertEqual(40, len(appdata.trucks))
        self.assertIsInstance(appdata.trucks[0], Truck)
        self.assertIsInstance(appdata.trucks, tuple)

    def test_createSingleTruckFunction_whenAllParamsArevalid(self):
        appdata = AppData()
        truck_manager = TruckManager(appdata, False)

        result = truck_manager.create_single_truck('Scania', 42000, 8000)

        self.assertEqual(len(appdata.trucks), 1)
        self.assertIsInstance(appdata.trucks[0], Truck)
        self.assertEqual(None, result)
