# Program to calculate hotel room bill

import os

def calculate_bill(room_type, days):
    rates = {
        "standard": 2000,
        "deluxe": 3000,
        "suite": 4000
    }

    rate = rates.get(room_type.lower(), 2000)
    return rate * days


if __name__ == "__main__":
    print("=== Hotel Room Billing System ===")

    # Read values from Jenkins environment variables
    name = os.getenv("customer_name", "Guest")
    room_type = os.getenv("room_type", "standard")
    days = int(os.getenv("days_stayed", "1"))

    total_bill = calculate_bill(room_type, days)

    print("\n--- BILL DETAILS ---")
    print("Customer Name :", name)
    print("Room Type     :", room_type)
    print("Days Stayed   :", days)
    print("Total Bill    : ₹", total_bill)

