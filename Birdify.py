def identify_bird_feather(color, length):
    bird_data = [
        {"name": "Sparrow", "color": "brown", "length": "2-3"},
        {"name": "Blue Jay", "color": "blue", "length": "5-7"},
        {"name": "Cardinal", "color": "red", "length": "3-4"},
        {"name": "Goldfinch", "color": "yellow", "length": "2-3"},
        {"name": "Robin", "color": "orange", "length": "4-5"}
    ]

    # Standardize input
    color = color.lower().strip()
    length = float(length)

    # Compare input with bird data
    for bird in bird_data:
        if bird["color"] == color:
            min_length, max_length = map(float, bird["length"].split("-"))
            if min_length <= length <= max_length:
                return bird["name"]

    return "Unknown bird"