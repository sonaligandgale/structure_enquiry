# Program to calculate hotel room bill

import sys

def calculate_bill(room_type, days):
    if room_type.lower() == "standard":
        rate = 1500
    elif room_type.lower() == "deluxe":
        rate = 2500
    elif room_type.lower() == "suite":
        rate = 4000
    else:
        return -1
    return rate * days


if __name__ == "__main__":
    print("=== Hotel Room Billing System ===")

    try:
        # Command line input
        if len(sys.argv) == 4:
            name = sys.argv[1]
            room_type = sys.argv[2]
            days = int(sys.argv[3])

        # User input
        else:
            name = input("Enter Customer Name: ")
            room_type = input("Enter Room Type (Standard/Deluxe/Suite): ")
            days = int(input("Enter Number of Days Stayed: "))

        total_bill = calculate_bill(room_type, days)

        if total_bill == -1:
            print("Invalid room type entered.")
        else:
            print("\n--- BILL DETAILS ---")
            print("Customer Name :", name)
            print("Room Type     :", room_type)
            print("Days Stayed   :", days)
            print("Total Bill    : ₹", total_bill)

    except ValueError:
        print("Invalid input. Please enter valid numeric values.")
