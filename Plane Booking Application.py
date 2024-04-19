class Burak757:
    def __init__(self):
        self.seat_bookings = {} # Initialise an empty dictionary to store seat bookings

        # Define the layout of the Burak757 floor plan
        self.num_rows = 7    # There would be 7 rows, A-F rows and X aisle
        self.num_columns = 80
        self.floor_plan = []    # Initialise an empty list to illustrate the floor plan

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
                    updated_row.append(f"{seat} R")  # Add 'R' for booked seats
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
            print(f"Seat {seat_number} is available.")  # Print if the seat is available

    # Function to book a seat
    def book_seat(self, seat_number):
        if seat_number in self.seat_bookings:  # Check if the seat is already booked
            print(f"Seat {seat_number} is already booked.")
        else:
            # Check if the seat is aisle, storage area, or already booked
            if seat_number in ["77D", "77E", "77F", "78D", "78E", "78F", "X", "S"]:
                print("Sorry, the seat you are trying to book is either an aisle or part of the storage area.")
            else:
                self.seat_bookings[seat_number] = "R"  # Book the seat
                print(f"Seat {seat_number} has been booked successfully.")
                self.display_floor_plan()  # Update floor plan after booking

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

if __name__ == "__main__":
    burak757 = Burak757()
    burak757.main()