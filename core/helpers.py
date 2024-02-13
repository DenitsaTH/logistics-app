import os

def ensure_valid_params_count(min_expected_count=0, actual_params=0, max_expected=0):
    if min_expected_count == max_expected and min_expected_count != actual_params:
        return False
    if min_expected_count != 0 and min_expected_count <= actual_params:
        return True
    if max_expected != 0 and max_expected >= actual_params:
        return True
    return False


def check_if_valid_stop(stops):
    for stop in stops:
        if stop.lower() not in ['syd', 'mel', 'adl', 'asp', 'bri', 'dar', 'per']:
            return False
    return True    
    

def parse_to_integer(s):
    try:
        return int(s)
    except ValueError:
        return
    

def file_is_empty(path):
    return  True if os.stat(path).st_size==0 else False
