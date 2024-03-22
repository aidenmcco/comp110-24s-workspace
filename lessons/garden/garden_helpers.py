"""Some functions for my garden plan!"""

__author__ = "730522247"


def add_by_kind(input_dictionary: dict[str, list[str]], kind: str, plant: str) -> None:
    """Add plant under its kind."""
    if kind in input_dictionary:
        input_dictionary[kind].append(plant)
    else:
        input_dictionary[kind] = []
        input_dictionary[kind].append(plant)


def add_by_date(input_dictionary: dict[str, list[str]], date: str, plant: str) -> None:
    """Add plant under date to sow seeds."""
    if date in input_dictionary:
        input_dictionary[date].append(plant)
    else:
        input_dictionary[date] = []
        input_dictionary[date].append(plant)


def lookup_by_kind_and_date(plant_dictionary: dict[str, list[str]], date_dictionary: dict[str, list[str]], kind: str, date: str) -> str:
    """Lookup plants of a certain kind to plant at a certain date."""
    assert kind in plant_dictionary
    assert date in date_dictionary
    plant_list: list[str] = plant_dictionary[kind]
    date_list: list[str] = date_dictionary[date]
    combined_list: list[str] = []
    for plant in plant_list:
        for other_plant in date_list:
            if plant == other_plant:
                combined_list.append(other_plant)
        if len(combined_list) > 0:
            return f"{kind}s to plant in {date}: {combined_list}"
        else:
            return f"no {kind}s to plant in {date}."