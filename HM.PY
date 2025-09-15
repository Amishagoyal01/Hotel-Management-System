import random

# Dictionaries to store data
existing_customers = {
    101: {"Name": "Anshuman", "Phone Number": 991489461, "Bill": 0, "Bookings": {}}
}
X = {}  # Food orders will be stored here


# Start the program
def HMS():
    print("\n--- Hotel Management System ---")
    print("1. Bookings")
    print("2. Food Orders")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("1. Existing User")
        print("2. New User")
        choice2 = int(input("Enter your choice: "))
        if choice2 == 1:
            existing_user()
        elif choice2 == 2:
            new_user()
        else:
            print("Invalid choice")
            HMS()
    elif choice == 2:
        print("1. Existing Food Customer")
        print("2. New Food Customer")
        choice2 = int(input("Enter your choice: "))
        if choice2 == 1:
            old_customers()
        elif choice2 == 2:
            new_customers()
        else:
            print("Invalid choice")
            HMS()
    else:
        print("Invalid choice")
        HMS()


# Existing user
def existing_user():
    b = int(input("Enter your Booking ID: "))
    if b in existing_customers:
        print(f"Welcome back, {existing_customers[b]['Name']}")
        bookings(b)
    else:
        print("Booking ID not found.")
        existing_user()


# New user
def new_user():
    name = input("Enter your name: ")
    phone = int(input("Enter your phone number: "))
    Booking_id = random.randint(100, 500)
    existing_customers[Booking_id] = {
        "Name": name,
        "Phone Number": phone,
        "Bill": 0,
        "Bookings": {}
    }
    print(f"Booking created successfully! Your Booking ID: {Booking_id}")
    bookings(Booking_id)


# Booking choices
def bookings(Booking_id):
    print("\n--- Booking Options ---")
    print("1. Room Booking")
    print("2. Hall Booking")
    print("3. Table Booking")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        room_booking(Booking_id)
    elif choice == 2:
        hall_booking(Booking_id)
    elif choice == 3:
        table_booking(Booking_id)
    else:
        print("Invalid choice")
        bookings(Booking_id)


# Room Booking
def room_booking(Booking_id):
    print("\n--- Room Types ---")
    print("1. Single Seater: 1200 per day")
    print("2. Double Seater: 2000 per day")
    print("3. Mini Suite: 3500 per day")
    print("4. Suite: 5000 per day")
    choice = int(input("Enter room choice: "))
    prices = {1: 1200, 2: 2000, 3: 3500, 4: 5000}
    if choice in prices:
        check_in = input("Enter check-in date (dd/mm/yyyy): ")
        check_out = input("Enter check-out date (dd/mm/yyyy): ")
        days = int(input("Enter number of days for stay: "))

        num_persons = 1
        if choice >= 3:
            num_persons = int(input("Enter number of persons staying: "))

        stay_cost = prices[choice] * days
        existing_customers[Booking_id]["Bill"] += stay_cost
        existing_customers[Booking_id]["Bookings"]["Room"] = {
            "Type": choice,
            "Check-in": check_in,
            "Check-out": check_out,
            "Days": days,
            "Persons": num_persons,
            "Room Cost": stay_cost
        }
        print(f"Room booked successfully from {check_in} to {check_out} "
              f"for {days} days! Room bill: {stay_cost}")
        print("Current total bill:", existing_customers[Booking_id]["Bill"])
        ask_food_order(Booking_id)
    else:
        print("Invalid choice")
        room_booking(Booking_id)


# Hall Booking
def hall_booking(Booking_id):
    print("\n--- Hall Booking ---")
    name = input("Enter your name: ")
    purpose = input("Purpose of hall booking: ")
    date = input("Enter date (dd/mm/yyyy): ")
    timings = input("Enter timing: ")
    num_persons = int(input("Number of persons attending: "))
    if 80 <= num_persons <= 120:
        existing_customers[Booking_id]["Bill"] += 12000
        existing_customers[Booking_id]["Bookings"]["Hall"] = {
            "Name": name,
            "Purpose": purpose,
            "Date": date,
            "Timings": timings,
            "Persons": num_persons
        }
        print("Hall booked successfully! Booking bill:",
              existing_customers[Booking_id]["Bill"])
        ask_food_order(Booking_id)
    else:
        print("Hall can accommodate 80 to 120 people only.")
        hall_booking(Booking_id)


# Table Booking
def table_booking(Booking_id):
    print("\n--- Table Types ---")
    print("1. 2-Seater: 2500")
    print("2. 4-Seater: 4500")
    print("3. 6-Seater: 6500")
    choice = int(input("Enter your choice: "))
    prices = {1: 2500, 2: 4500, 3: 6500}
    if choice in prices:
        name = input("Enter your name: ")
        date = input("Enter date (dd/mm/yyyy): ")
        timing = input("Enter timing: ")
        existing_customers[Booking_id]["Bill"] += prices[choice]
        existing_customers[Booking_id]["Bookings"]["Table"] = {
            "Name": name,
            "Date": date,
            "Timing": timing,
            "Type": choice
        }
        print("Table booked successfully! Booking bill:",
              existing_customers[Booking_id]["Bill"])
        ask_food_order(Booking_id)
    else:
        print("Invalid choice")
        table_booking(Booking_id)


# Ask for food order
def ask_food_order(Booking_id):
    print("\nDo you want to order food?")
    print("1. Yes")
    print("2. No")
    choice = int(input("Enter choice: "))
    if choice == 1:
        new_food_order(Booking_id)
    elif choice == 2:
        print("Thanks! Your total bill is:", existing_customers[Booking_id]["Bill"])
    else:
        print("Invalid choice")
        ask_food_order(Booking_id)


# Food ordering for booking
def new_food_order(Booking_id):
    order_id = random.randint(100, 500)
    X[order_id] = {
        "Name": existing_customers[Booking_id]["Name"],
        "Phone Number": existing_customers[Booking_id]["Phone Number"],
        "Bill": 0
    }
    menu(order_id, Booking_id)


# Food menu
def menu(order_id, Booking_id):
    print("\n--- Food Menu ---")
    print("1. Veg")
    print("2. Non-Veg")
    print("3. Drinks")
    print("4. Desserts")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        veg_menu(order_id, Booking_id)
    elif choice == 2:
        non_veg_menu(order_id, Booking_id)
    elif choice == 3:
        drinks(order_id, Booking_id)
    elif choice == 4:
        desserts(order_id, Booking_id)
    else:
        print("Invalid choice")
        menu(order_id, Booking_id)


def veg_menu(order_id, Booking_id):
    print("1. Dal Makhani: 300")
    print("2. Shahi Paneer: 500")
    choice = int(input("Enter your choice: "))
    prices = {1: 300, 2: 500}
    if choice in prices:
        X[order_id]["Bill"] += prices[choice]
        continue_food_order(order_id, Booking_id)
    else:
        print("Invalid choice")
        veg_menu(order_id, Booking_id)


def non_veg_menu(order_id, Booking_id):
    print("1. Chicken Curry: 350")
    print("2. Fish Fry: 400")
    choice = int(input("Enter your choice: "))
    prices = {1: 350, 2: 400}
    if choice in prices:
        X[order_id]["Bill"] += prices[choice]
        continue_food_order(order_id, Booking_id)
    else:
        print("Invalid choice")
        non_veg_menu(order_id, Booking_id)


def drinks(order_id, Booking_id):
    print("1. Coke: 50")
    print("2. Cold Coffee: 120")
    choice = int(input("Enter your choice: "))
    prices = {1: 50, 2: 120}
    if choice in prices:
        X[order_id]["Bill"] += prices[choice]
        continue_food_order(order_id, Booking_id)
    else:
        print("Invalid choice")
        drinks(order_id, Booking_id)


def desserts(order_id, Booking_id):
    print("1. Ice Cream: 80")
    print("2. Gulab Jamun: 100")
    choice = int(input("Enter your choice: "))
    prices = {1: 80, 2: 100}
    if choice in prices:
        X[order_id]["Bill"] += prices[choice]
        continue_food_order(order_id, Booking_id)
    else:
        print("Invalid choice")
        desserts(order_id, Booking_id)


def continue_food_order(order_id, Booking_id):
    print("\n1. Exit")
    print("2. Continue Ordering")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        if Booking_id is not None:
            total_bill = existing_customers[Booking_id]["Bill"] + X[order_id]["Bill"]
        else:
            total_bill = X[order_id]["Bill"]
        print("Your total bill is:", total_bill)
        HMS()
    elif choice == 2:
        menu(order_id, Booking_id)
    else:
        print("Invalid choice")
        continue_food_order(order_id, Booking_id)


# Existing food customer
def old_customers():
    order_id = int(input("Enter your Order ID: "))
    if order_id in X:
        print(f"Welcome back, {X[order_id]['Name']}")
        menu(order_id, None)
    else:
        print("Order ID not found.")
        old_customers()


# New food customer
def new_customers():
    name = input("Enter your name: ")
    phone = int(input("Enter your phone number: "))
    order_id = random.randint(100, 500)
    X[order_id] = {"Name": name, "Phone Number": phone, "Bill": 0}
    print(f"Your Order ID is: {order_id}")
   
    menu(order_id, None)


# Start the system
HMS()
