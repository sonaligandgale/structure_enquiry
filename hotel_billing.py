# Program to calculate hotel room bill
import os

def calculate_bill(room_type, days):
    room_type = room_type.lower()

    if days <= 0:
        return -1

    if room_type == "standard":
        return 1500 * days
    elif room_type == "deluxe":
        return 2500 * days
    else:
        return -1


if __name__ == "__main__":
    name = os.getenv("CUSTOMER_NAME", "Guest")
    room_type = os.getenv("ROOM_TYPE", "standard")
    days = int(os.getenv("DAYS_STAYED", "1"))

    total_bill = calculate_bill(room_type, days)

    print("=== Hotel Room Billing System ===")
    print("Customer Name :", name)
    print("Room Type     :", room_type)
    print("Days Stayed   :", days)

    if total_bill == -1:
        print("Invalid input")
    else:
        print("Total Bill : Rs.", total_bill)
