def get_keys_with_top_values(my_dict):
    return[
        key
        for (key, value) in my_dict.items()
        if value == max(my_dict.values())
    ]
