import csv
import random
import string


class Burak757:
    def __init__(self):
        # Initialize an empty dictionary to store seat bookings with booking references
        self.seat_bookings = {}

        # Define the layout of the Burak757 floor plan
        self.num_rows = 7  # There would be 7 rows, A-F rows and X aisle
        self.num_columns = 80
        self.floor_plan = []

        # Generate floor plan
        for row_num in range(self.num_rows):  # Loop through each row
            row = []  # Initialize an empty list for each row
            for col_num in range(self.num_columns):  # Loop through each column
                if row_num == 3:  # Check if it's the aisle row
                    row.append("X   ")  # Aisle or storage area
                else:
                    if row_num <= 3:  # Check if it's rows A-C
                        row.append(f"{col_num + 1}{chr(65 + row_num)}")  # Seats for rows A-C
                    else:
                        # Seats for rows D-F
                        seat = f"{col_num + 1}{chr(64 + row_num)}"
                        # Mark specified seats as storage area
                        if (col_num == 76 and row_num in [4, 5, 6]) or (col_num == 77 and row_num in [4, 5, 6]):
                            seat = "S   "
                        row.append(seat)  # Append seat to the row
            self.floor_plan.append(row)  # Append the row to the floor plan

    # Function to display the floor plan table
    def display_floor_plan(self):
        print("Floor Plan:")
        for row_num, row in enumerate(self.floor_plan):  # Loop through each row
            updated_row = []  # Initialize an empty list for the updated row
            for seat in row:  # Loop through each seat in the row
                if seat in self.seat_bookings:  # Check if the seat is booked
                    reference = self.seat_bookings[seat][0]  # Get booking reference
                    updated_row.append(f"{seat} {reference}")  # Add seat label with booking reference
                elif seat in ["X   ", "S   "]:  # Check if it's aisle or storage area
                    updated_row.append(seat)  # Don't add any label after 'X' or 'S'
                else:
                    updated_row.append(f"{seat} F")  # Add 'F' for free seats
            print("\t".join(updated_row))  # Print the row with tabs between seats

    # Function to check the availability of a seat
    def check_availability(self, seat_number):
        if seat_number in self.seat_bookings:  # Check if the seat is booked
            print(f"Seat {seat_number} is already booked.")
        else:
            print(f"Seat {seat_number} is available.")  # Print if the seat is available.

    # Function to book a seat
    def book_seat(self, seat_number):
        # Check if the seat is already booked
        if seat_number in self.seat_bookings:
            print(f"Seat {seat_number} is already booked.")
            return

        # Validate if the seat number is within the valid range
        if not (seat_number[:-1].isdigit() and 1 <= int(seat_number[:-1]) <= self.num_columns):
            print("Invalid seat number. Please enter a valid seat number.")
            return

        # Validate if the seat letter is within the valid range
        if not (seat_number[-1].isalpha() and ord(seat_number[-1].upper()) - ord('A') < self.num_rows):
            print("Invalid seat number. Please enter a valid seat number.")
            return

        # Check if the seat is aisle, storage area, or already booked
        if seat_number in ["77D", "77E", "77F", "78D", "78E", "78F", "X", "S"]:
            print("Sorry, the seat you are trying to book is either an aisle or part of the storage area.")
        else:
            booking_reference = self.generate_booking_reference()  # Generate booking reference
            passport_number, first_name, last_name = self.get_user_details()  # Get user details
            self.seat_bookings[seat_number] = (
            booking_reference, passport_number, first_name, last_name)  # Book the seat with booking reference
            print(f"Seat {seat_number} has been booked successfully with booking reference {booking_reference}.")
            self.save_booking_details_to_csv(seat_number, booking_reference, passport_number, first_name,
                                             last_name)  # Save booking details to CSV
            self.display_floor_plan()  # Update floor plan after booking

    # Function to generate a random alphanumeric booking reference
    def generate_booking_reference(self):
        while True:
            reference = ''.join(
                random.choices(string.ascii_uppercase + string.digits, k=8))  # Generate random reference
            if reference not in [booking[0] for booking in self.seat_bookings.values()]:  # Check if reference is unique
                return reference

    # Function to gather user details for booking
    def get_user_details(self):
        passport_number = input("Enter passport number: ")
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        return passport_number, first_name, last_name

    # Function to save booking details to a CSV file
    def save_booking_details_to_csv(self, seat_number, booking_reference, passport_number, first_name, last_name):
        with open('booking_details.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([f"Booking for {first_name} {last_name}", f"Seat Label: {seat_number}",
                             f"Booking Reference: {booking_reference}", f"Passport Number: {passport_number}",
                             f"First Name: {first_name}", f"Last Name: {last_name}"])

    # Function to free a booked seat
    def free_seat(self, seat_number):
        if seat_number in self.seat_bookings:  # Check if the seat is booked
            del self.seat_bookings[seat_number]  # Remove the booking
            print(f"Seat {seat_number} has been freed successfully.")
            self.display_floor_plan()  # Update floor plan after freeing
        else:
            print(f"Seat {seat_number} is not booked.")  # Print if the seat is not booked.

    # Function to show the booking state
    def show_booking_state(self):
        print("Booking State:")
        for seat, (reference, _, _, _) in self.seat_bookings.items():  # Loop through booked seats
            print(f"Seat {seat}: Booked with booking reference {reference}")  # Print booking reference

    # Main function to display the menu and handle user input
    def main(self):
        while True:
            print("\nMenu:")
            print("1. Display floor plan")
            print("2. Check availability of seat")
            print("3. Book a seat")
            print("4. Free a seat")
            print("5. Show booking state")
            print("6. Exit program")

            choice = input("Enter your choice: ")  # Get user input for choice

            if choice == "1":
                self.display_floor_plan()  # Display floor plan
            elif choice == "2":
                seat_number = input("Enter seat number to check availability (e.g., 1A): ").upper()
                self.check_availability(seat_number)  # Check availability of seat
            elif choice == "3":
                seat_number = input("Enter seat number to book (e.g., 1A): ").upper()
                self.book_seat(seat_number)  # Book a seat
            elif choice == "4":
                seat_number = input("Enter seat number to free (e.g., 1A): ").upper()
                self.free_seat(seat_number)  # Free a seat
            elif choice == "5":
                self.show_booking_state()  # Show booking state
            elif choice == "6":
                print("Exiting program.")  # Exit the program
                break
            else:
                print("Invalid choice. Please enter a valid option.")  # Print for invalid choice


if __name__ == "__main__":
    burak757 = Burak757()
    burak757.main()
