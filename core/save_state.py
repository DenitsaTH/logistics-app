from datetime import datetime
from core.app_data import AppData


def save_state(app_data: AppData):
    with open('db/packages.txt', 'w') as txt_file:
        for p in app_data.packages:
            txt_file.write(f'{p.start_location} {p.end_location} {p.weight} {p.contact_info.first_name} {p.contact_info.last_name} {p.contact_info.email} {p.is_assigned} {p.connected_route}' + '\n')

    with open('db/trucks.txt', 'w') as txt_file:
        for t in app_data.trucks:
            txt_file.write(f'{t.brand} {t.capacity} {t.km_range} {len(t.taken_time_slots)}' + '\n')
            for key, value in t.taken_time_slots.items():
                value = [datetime.strftime(v, "%Y-%m-%d %H:%M:%S") for v in value]
                txt_file.write(f'{key}  {'_'.join(value)}' + '\n')

    with open('db/routes.txt', 'w') as txt_file:
        for r in app_data.routes:
            if r.truck is None:
                truck_id = -1
            else:
                truck_id = r.truck.id
            txt_file.write(f'{','.join([str(x) for x in r.distances])} {datetime.strftime(r.departure_time, "%Y-%m-%d %H:%M:%S")} {','.join(r.stops)} {str(truck_id)} {','.join([str(x) for x in r.delivery_weight_per_stop])}')
