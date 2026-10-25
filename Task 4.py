from abc import ABC, abstractmethod
from datetime import datetime


# -------------------------------
# Flight Class
# -------------------------------
class Flight:
    def __init__(self, code, airline, source, destination,
                 seats, base_fare):
        self.__code = code
        self.__airline = airline
        self.__source = source
        self.__destination = destination
        self.__seats = seats
        self.__base_fare = base_fare

    @property
    def code(self):
        return self.__code

    @property
    def airline(self):
        return self.__airline

    @property
    def source(self):
        return self.__source

    @property
    def destination(self):
        return self.__destination

    @property
    def seats(self):
        return self.__seats

    @property
    def base_fare(self):
        return self.__base_fare

    def display_flight(self):
        print(
            f"{self.code:<10} {self.airline:<15} "
            f"{self.source:<15} {self.destination:<15} "
            f"{self.seats:<10} Rs.{self.base_fare:.2f}"
        )

    def book_seats(self, count):
        if count <= 0:
            return False

        if count > self.__seats:
            return False

        self.__seats -= count
        return True


# -------------------------------
# Abstract Passenger Class
# -------------------------------
class Passenger(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_discount(self):
        pass

    def display_details(self):
        print(f"Passenger Name : {self.name}")
        print(f"Passenger Age  : {self.age}")
        print(f"Category       : {self.__class__.__name__}")


# -------------------------------
# Passenger Inheritance
# -------------------------------
class RegularPassenger(Passenger):
    def get_discount(self):
        return 0


class StudentPassenger(Passenger):
    def get_discount(self):
        return 10


# -------------------------------
# Booking Class
# -------------------------------
class Booking:
    def __init__(self, booking_id, passenger, flight,
                 ticket_count, base_total, discount, final_total):
        self.booking_id = booking_id
        self.passenger = passenger
        self.flight = flight
        self.ticket_count = ticket_count
        self.base_total = base_total
        self.discount = discount
        self.final_total = final_total
        self.booking_time = datetime.now().strftime(
            "%d-%m-%Y %I:%M %p"
        )

    def display_summary(self):
        print("\n" + "=" * 50)
        print("             BOOKING SUMMARY")
        print("=" * 50)
        print(f"Booking ID       : {self.booking_id}")
        print(f"Booking Date     : {self.booking_time}")

        self.passenger.display_details()

        print("-" * 50)
        print(f"Flight Code      : {self.flight.code}")
        print(f"Airline          : {self.flight.airline}")
        print(f"From             : {self.flight.source}")
        print(f"To               : {self.flight.destination}")
        print(f"Number of Tickets: {self.ticket_count}")
        print(f"Base Fare Total  : Rs.{self.base_total:.2f}")
        print(f"Discount         : Rs.{self.discount:.2f}")
        print(f"Final Amount     : Rs.{self.final_total:.2f}")
        print("=" * 50)
        print("Booking confirmed successfully!")


# -------------------------------
# Flight Booking System
# -------------------------------
class FlightBookingSystem:
    def __init__(self):
        self.flights = [
            Flight("AI101", "Air India", "Mumbai",
                   "Delhi", 10, 4500),
            Flight("6E202", "IndiGo", "Delhi",
                   "Bengaluru", 8, 3800),
            Flight("UK303", "Vistara", "Mumbai",
                   "Chennai", 6, 5200),
            Flight("AI404", "Air India", "Pune",
                   "Hyderabad", 5, 3200)
        ]

        self.bookings = []
        self.booking_counter = 1001

    # Display all available flights
    def view_flights(self):
        print("\n" + "=" * 85)
        print("                     AVAILABLE FLIGHTS")
        print("=" * 85)
        print(
            f"{'Code':<10} {'Airline':<15} {'Source':<15} "
            f"{'Destination':<15} {'Seats':<10} {'Base Fare'}"
        )
        print("-" * 85)

        for flight in self.flights:
            flight.display_flight()

        print("=" * 85)

    # Find flight using flight code
    def find_flight(self, code):
        for flight in self.flights:
            if flight.code.lower() == code.lower():
                return flight
        return None

    # Calculate fare
    def calculate_fare(self, flight, passenger, ticket_count):
        base_total = flight.base_fare * ticket_count
        discount = base_total * passenger.get_discount() / 100
        final_total = base_total - discount

        return base_total, discount, final_total

    # Book a flight
    def book_flight(self):
        self.view_flights()

        code = input("\nEnter flight code: ").strip()
        flight = self.find_flight(code)

        if flight is None:
            print("Error: Invalid flight code.")
            return

        if flight.seats == 0:
            print("Sorry, no seats are available.")
            return

        name = input("Enter passenger name: ").strip()

        if not name or not any(ch.isalpha() for ch in name):
            print("Error: Enter a valid passenger name.")
            return

        try:
            age = int(input("Enter passenger age: "))

            if age < 1 or age > 120:
                print("Error: Age must be between 1 and 120.")
                return

            ticket_count = int(input("Enter number of tickets: "))

            if ticket_count < 1:
                print("Error: At least one ticket is required.")
                return

            if ticket_count > flight.seats:
                print(
                    f"Error: Only {flight.seats} seats are available."
                )
                return

            print("\nPassenger Category")
            print("1. Regular Passenger")
            print("2. Student Passenger")

            category = input("Choose category (1 or 2): ").strip()

            if category == "1":
                passenger = RegularPassenger(name, age)
            elif category == "2":
                passenger = StudentPassenger(name, age)
            else:
                print("Error: Invalid passenger category.")
                return

        except ValueError:
            print("Error: Please enter valid numeric values.")
            return

        # Calculate fare before confirming the booking
        base_total, discount, final_total = self.calculate_fare(
            flight, passenger, ticket_count
        )

        print("\n---------- FARE DETAILS ----------")
        print(f"Base fare per ticket : Rs.{flight.base_fare:.2f}")
        print(f"Number of tickets    : {ticket_count}")
        print(f"Base fare total      : Rs.{base_total:.2f}")
        print(f"Discount percentage  : {passenger.get_discount()}%")
        print(f"Discount amount      : Rs.{discount:.2f}")
        print(f"Final amount         : Rs.{final_total:.2f}")
        print("----------------------------------")

        confirm = input("Confirm booking? (yes/no): ").strip().lower()

        if confirm not in ("yes", "y"):
            print("Booking cancelled. No seats were changed.")
            return

        # Update seats only after confirmation
        if not flight.book_seats(ticket_count):
            print("Booking failed: Seats are no longer available.")
            return

        booking = Booking(
            f"BK{self.booking_counter}",
            passenger,
            flight,
            ticket_count,
            base_total,
            discount,
            final_total
        )

        self.bookings.append(booking)
        self.booking_counter += 1

        booking.display_summary()

    # Display the most recent confirmed booking
    def view_booking(self):
        if not self.bookings:
            print("\nNo confirmed bookings found.")
            return

        self.bookings[-1].display_summary()

    # Main menu
    def run(self):
        print("\nWelcome to Flight Booking System!")

        while True:
            print("\n========== MAIN MENU ==========")
            print("1. View Flights")
            print("2. Book Flight")
            print("3. View Booking")
            print("4. Exit")
            print("===============================")

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.view_flights()

            elif choice == "2":
                self.book_flight()

            elif choice == "3":
                self.view_booking()

            elif choice == "4":
                print("Thank you for using Flight Booking System!")
                print("Goodbye!")
                break

            else:
                print("Invalid choice. Please select 1, 2, 3, or 4.")


# -------------------------------
# Program Entry Point
# -------------------------------
if __name__ == "__main__":
    system = FlightBookingSystem()
    system.run()
