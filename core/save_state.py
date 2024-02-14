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
