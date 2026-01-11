# ===============================
# HOTEL BILLING TEST CASES
# ===============================

from hotel_billing import calculate_bill


# -------- STANDARD ROOM TEST CASES --------

def test_standard_room_lower_boundary():
    bill = calculate_bill("standard", 1)
    assert bill == 1500

def test_standard_room_middle_value():
    bill = calculate_bill("standard", 3)
    assert bill == 4500

def test_standard_room_upper_boundary():
    bill = calculate_bill("standard", 5)
    assert bill == 7500


# -------- DELUXE ROOM TEST CASES --------

def test_deluxe_room_lower_boundary():
    bill = calculate_bill("deluxe", 1)
    assert bill == 2500

def test_deluxe_room_middle_value():
    bill = calculate_bill("deluxe", 4)
    assert bill == 10000

def test_deluxe_room_upper_boundary():
    bill = calculate_bill("deluxe", 6)
    assert bill == 15000


# -------- SUITE ROOM TEST CASES --------

def test_suite_room_lower_boundary():
    bill = calculate_bill("suite", 1)
    assert bill == 4000

def test_suite_room_middle_value():
    bill = calculate_bill("suite", 3)
    assert bill == 12000

def test_suite_room_upper_boundary():
    bill = calculate_bill("suite", 5)
    assert bill == 20000


# -------- INVALID ROOM TYPE TEST CASE --------

def test_invalid_room_type():
    bill = calculate_bill("premium", 2)
    assert bill == -1
