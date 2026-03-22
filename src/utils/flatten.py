def flatten_json(data, parent_key='', sep='_'):
    items = []

    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key

        if isinstance(value, dict):
            items.extend(flatten_json(value, new_key, sep=sep).items())

        elif isinstance(value, list):
            # For now, just store list as-is (we’ll handle properly on Day 3)
            items.append((new_key, value))

        else:
            items.append((new_key, value))

    return dict(items)