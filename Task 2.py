# Cab Booking Chatbot

# Predefined route distances (in km)
distances = [5, 10, 15, 20, 25]

# Predefined cab rates per km
mini_rate = 12
sedan_rate = 15
suv_rate = 20

print("================================")
print("     CAB BOOKING CHATBOT")
print("================================")

while True:
    print("\nMAIN MENU")
    print("1. Book a Cab")
    print("2. View Cab Rates")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # Main menu choices
    if choice == "1":

        print("\nAVAILABLE CABS")
        print("1. Mini - Rs.", mini_rate, "per km")
        print("2. Sedan - Rs.", sedan_rate, "per km")
        print("3. SUV - Rs.", suv_rate, "per km")

        cab_choice = input("Choose your cab (1-3): ")

        # Select cab type
        if cab_choice == "1":
            cab_type = "Mini"
            rate = mini_rate

        elif cab_choice == "2":
            cab_type = "Sedan"
            rate = sedan_rate

        elif cab_choice == "3":
            cab_type = "SUV"
            rate = suv_rate

        else:
            print("Invalid cab choice! Please try again.")
            continue

        # Display available routes
        print("\nAVAILABLE ROUTES")

        for i in range(len(distances)):
            print(i + 1, ".", distances[i], "km")

        route_choice = input("Choose your route (1-5): ")

        # Validate route choice
        if route_choice not in ["1", "2", "3", "4", "5"]:
            print("Invalid route choice! Please try again.")
            continue

        distance = distances[int(route_choice) - 1]

        # Calculate fare
        fare = distance * rate

        # Display booking details
        print("\n========== BOOKING DETAILS ==========")
        print("Cab Type :", cab_type)
        print("Distance :", distance, "km")
        print("Rate     : Rs.", rate, "per km")
        print("Total Fare: Rs.", fare)
        print("=====================================")

        # Confirm booking
        confirm = input("Confirm booking? (yes/no): ")

        if confirm.lower() == "yes":
            print("\nCab booked successfully!")
            print("Thank you for choosing our service.")
        else:
            print("Booking cancelled.")

    elif choice == "2":

        # Display cab rates
        print("\n========== CAB RATES ==========")
        print("Mini  : Rs.", mini_rate, "per km")
        print("Sedan : Rs.", sedan_rate, "per km")
        print("SUV   : Rs.", suv_rate, "per km")
        print("===============================")

    elif choice == "3":

        # Exit the program
        print("\nThank you for using Cab Booking Chatbot!")
        break

    else:
        print("Invalid menu choice! Please enter 1, 2, or 3.")
