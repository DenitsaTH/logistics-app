from datetime import datetime
from managers.package_manager import PackageManager
from managers.truck_manager import TruckManager
from managers.route_manager import RouteManager
from core.app_data import AppData


def load_state(package_manager: PackageManager, truck_manager: TruckManager, route_manager: RouteManager, app_data: AppData):
    with open('db/packages.txt', 'r') as txt_file:
        for line in txt_file.readlines():
            start_location, end_location, weight, *customer_info, is_assigned, connected_route = line.split()
            package_manager.log_package(start_location, end_location, weight, *customer_info, is_assigned=is_assigned, connected_route=connected_route)


    with open('db/trucks.txt', 'r') as txt_file:
        trucks_list = txt_file.readlines()
        current_idx = 0

        while current_idx != len(trucks_list) - 2:
            line = trucks_list[current_idx]
            brand, capacity, km_range, taken_time_slots_count = line.split()
            time_slots = {}
            capacity = int(capacity)
            km_range = int(km_range)
            taken_time_slots_count = int(taken_time_slots_count)
            current_idx += 1

            if taken_time_slots_count:
                for i in range(taken_time_slots_count):
                    line = trucks_list[current_idx]
                    route_id, slots = line.split('  ')
                    start_time, end_time = slots.split('_')
                    end_time = end_time.rstrip()
                    route_id = int(route_id)
                    start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
                    end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
                    time_slots[route_id] = [start_time, end_time]

                    current_idx += 1
            
            truck_manager.create_single_truck(brand, capacity, km_range, time_slots)


    with open('db/routes.txt', 'r') as txt_file:
        for line in txt_file.readlines():
            distances, departure_d, departure_h, stops, truck_id, delivery_weight_per_stop = line.split()
            distances = [int(x) for x in distances.split(',')]
            departure_time = f'{departure_d} {departure_h}'
            departure_time = datetime.strptime(departure_time, "%Y-%m-%d %H:%M:%S")
            stops = stops.split(',')
            truck_id = int(truck_id)
            delivery_weight_per_stop = [float(x) for x in delivery_weight_per_stop.split(',')]
            route_manager.generate_route_from_file(distances, departure_time, stops, truck_id, delivery_weight_per_stop)
