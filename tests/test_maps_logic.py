from app.maps_logic import format_time_to_mins, get_time_to_destination, get_suitable_postcodes


def test_format_time_to_mins():
    assert format_time_to_mins(60) == 1  # 60 seconds
    assert format_time_to_mins(50) == 1  # 50 seconds rounded up
    assert format_time_to_mins(25) == 0  # 25 seconds rounded down


def test_get_time_to_destination():
    assert get_time_to_destination("EC2M 7PY", "NW1 6JJ") < 30


def test_get_suitable_postcodes():
    mock_postcodes_to_check = ["IG12UT", "N153NX"]
    office_postcode = "NW16JJ"
    commute_time = 60
    assert get_suitable_postcodes(mock_postcodes_to_check, office_postcode, commute_time) == {"Postcodes": ["N153NX"]}