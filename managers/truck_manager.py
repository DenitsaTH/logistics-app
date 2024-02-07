class TruckManager:
    trucks = {
        'Scania': {'next_id': 1001, 'end_id': 1010, 'capacity': 42000, 'max_range': 8000, 'number_of_vehicles': 10},
        'Man': {'next_id': 1011, 'end_id': 1025, 'capacity': 37000, 'max_range': 10000, 'number_of_vehicles': 15},
        'Actros': {'next_id': 1026, 'end_id': 1040, 'capacity': 26000, 'max_range': 13000, 'number_of_vehicles': 15}
    }


    def init(self, app_data):
        self.app_data = app_data

