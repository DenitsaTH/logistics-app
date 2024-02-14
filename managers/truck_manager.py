from models.truck import Truck
from core.app_data import AppData

class TruckManager:

    SCANIA_IDS = range(1001, 1011)
    MAN_IDS = range(1011, 1026)
    ACTROS_IDS = range(1026, 1041)
    STARTING_ID = 1001
    ENDING_ID = 1041

    garage = {
        'Scania': {'capacity': 42000, 'max_range': 8000},
        'Man': {'capacity': 37000, 'max_range': 10000},
        'Actros': {'capacity': 26000, 'max_range': 13000}
    }


    def __init__(self, app_data: AppData, should_open_garage: bool):
        self.app_data = app_data
        self.should_open_garage = should_open_garage
        if should_open_garage:
            self._open_garage()
        self.current_id = TruckManager.STARTING_ID


    def _open_garage(self):
        for id in range(TruckManager.STARTING_ID, TruckManager.ENDING_ID):
            if id in TruckManager.SCANIA_IDS:
                truck = Truck(id, 'Scania', TruckManager.garage['Scania']['capacity'], TruckManager.garage['Scania']['max_range'])
            elif id in TruckManager.MAN_IDS:
                truck = Truck(id, 'Man', TruckManager.garage['Man']['capacity'], TruckManager.garage['Man']['max_range'])
            else:
                truck = Truck(id, 'Actros', TruckManager.garage['Actros']['capacity'], TruckManager.garage['Actros']['max_range'])

            self.app_data.add_truck(truck)


    def create_single_truck(self, brand, capacity, km_range, time_slots=None):
        truck = Truck(self.current_id, brand, capacity, km_range, taken_time_slots=time_slots)
        self.app_data.add_truck(truck)
        self.current_id += 1
