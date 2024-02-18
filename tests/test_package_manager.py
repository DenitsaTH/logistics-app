from core.app_data import AppData
from models.customer import Customer
from models.package import Package
from core.helpers import ensure_valid_params_count
from managers.package_manager import PackageManager
import unittest


class PackageManager_Should(unittest.TestCase):
    def test_initializer_withValidAppDataAttribute(self):
        appdata = AppData()
        package_manager = PackageManager(appdata)
        self.assertEqual(appdata, package_manager.app_data)
        self.assertIsInstance(package_manager.app_data, AppData)

    def test_initializer_withNotValidAppDataAttribute(self):
        with self.assertRaises(ValueError):
            PackageManager('test')

    def test_logPackageFunction_whenAllParamsAreValid(self):
        appdata = AppData()
        package_manager = PackageManager(appdata)

        log_package_str = package_manager.log_package('BRI', 'MEL', 50, 'Test', 'Testov', 'test@gmail.com')
        package = appdata.packages[0]

        result_str = f"\nPackage successfully logged!\n{str(package)}"

        self.assertEqual(len(appdata.packages), 1)
        self.assertEqual('BRI', package.start_location)
        self.assertEqual(result_str, log_package_str)
        self.assertIsInstance(log_package_str, str)
        self.assertEqual(2, package_manager.id)
