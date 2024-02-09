def check_params_count(min_expected_count, actual_params, cmd_name):
    if min_expected_count > actual_params:
        raise ValueError(f'At least {min_expected_count} params expected for {cmd_name}')