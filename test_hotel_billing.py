from hotel_billing import calculate_bill

def test_standard_room_lower_boundary():
    assert calculate_bill("standard", 1) == 1500

def test_standard_room_middle_value():
    assert calculate_bill("standard", 3) == 4500

def test_standard_room_upper_boundary():
    assert calculate_bill("standard", 5) == 7500

def test_deluxe_room_lower_boundary():
    assert calculate_bill("deluxe", 1) == 2500

def test_deluxe_room_middle_value():
    assert calculate_bill("deluxe", 4) == 10000

def test_deluxe_room_upper_boundary():
    assert calculate_bill("deluxe", 6) == 15000

def test_invalid_room_type():
    assert calculate_bill("premium", 2) == -1

def test_invalid_days():
    assert calculate_bill("standard", 0) == -1
