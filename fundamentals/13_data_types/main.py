def add_data_types(object_one, object_two):
    if isinstance(object_one, dict) and isinstance(object_one, dict):
        return object_one | object_two
    return object_one + object_two
