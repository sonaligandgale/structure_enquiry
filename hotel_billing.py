# Program to calculate hotel room bill

def calculate_bill(room_type, days):
    if days <= 0:
        return -1

    room_type = room_type.lower()

    if room_type == "standard":
        rate = 1500
    elif room_type == "deluxe":
        rate = 2500
    else:
        return -1

    return rate * days


if __name__ == "__main__":
    
    name = "Guest"
    room_type = "standard"
    days = 1

    total_bill = calculate_bill(room_type, days)

    print("=== Hotel Room Billing System ===")
    print("\n--- BILL DETAILS ---")
    print("Customer Name :", name)
    print("Room Type     :", room_type)
    print("Days Stayed   :", days)
    print("Total Bill    : Rs.", total_bill)
