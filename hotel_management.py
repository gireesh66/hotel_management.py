import datetime

class Hotel:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = {i: {"available": True, "booked_by": None} for i in range(1, rooms + 1)}  # Room numbers start from 1
        self.bookings = {}  # Store booking details

    def display_available_rooms(self):
        print("\nAvailable Rooms:")
        for room_num, status in self.rooms.items():
            if status["available"]:
                print(f"Room {room_num}")

    def book_room(self, room_num, guest_name, check_in_date, check_out_date):
        if 1 <= room_num <= len(self.rooms):
            if self.rooms[room_num]["available"]:
                self.rooms[room_num]["available"] = False
                self.rooms[room_num]["booked_by"] = guest_name

                # Store booking details with dates as datetime objects
                check_in_date = datetime.datetime.strptime(check_in_date, "%Y-%m-%d").date()
                check_out_date = datetime.datetime.strptime(check_out_date, "%Y-%m-%d").date()

                booking_id = f"{guest_name}_{room_num}_{check_in_date.strftime('%Y%m%d')}" #Simple unique ID
                self.bookings[booking_id] = {
                    "room_num": room_num,
                    "guest_name": guest_name,
                    "check_in_date": check_in_date,
                    "check_out_date": check_out_date
                }

                print(f"Room {room_num} booked successfully for {guest_name}.")
                return booking_id  # Return the booking ID

            else:
                print(f"Room {room_num} is already booked.")
                return None
        else:
            print("Invalid room number.")
            return None

    def cancel_booking(self, booking_id):
        if booking_id in self.bookings:
            booking = self.bookings[booking_id]
            room_num = booking["room_num"]
            self.rooms[room_num]["available"] = True
            self.rooms[room_num]["booked_by"] = None
            del self.bookings[booking_id]
            print(f"Booking {booking_id} cancelled successfully.")
        else:
            print("Booking ID not found.")

    def find_booking(self, guest_name=None, room_num=None):
        found_bookings = []
        for booking_id, booking in self.bookings.items():
            if (guest_name is None or booking["guest_name"] == guest_name) and \
               (room_num is None or booking["room_num"] == room_num):
                found_bookings.append(booking)
        return found_bookings

    def display_booking_details(self, booking_id):
        if booking_id in self.bookings:
            booking = self.bookings[booking_id]
            print("\nBooking Details:")
            for key, value in booking.items():
                print(f"{key.capitalize()}: {value}")
        else:
            print("Booking ID not found.")


# Example Usage:
hotel = Hotel("Grand Hotel", 10)  # 10 rooms

while True:
    print("\nHotel Management System")
    print("1. Display Available Rooms")
    print("2. Book a Room")
    print("3. Cancel a Booking")
    print("4. Find Booking")
    print("5. Display Booking Details")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        hotel.display_available_rooms()
    elif choice == '2':
        room_num = int(input("Enter room number: "))
        guest_name = input("Enter guest name: ")
        check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
        check_out_date = input("Enter check-out date (YYYY-MM-DD): ")
        booking_id = hotel.book_room(room_num, guest_name, check_in_date, check_out_date)
        if booking_id:
            print(f"Your booking ID is: {booking_id}")
    elif choice == '3':
        booking_id = input("Enter booking ID to cancel: ")
        hotel.cancel_booking(booking_id)
    elif choice == '4':
        guest_name = input("Enter guest name (or press Enter to search by room): ")
        room_num = input("Enter room number (or press Enter to search by guest): ")
        room_num = int(room_num) if room_num else None # Convert to int if provided
        bookings = hotel.find_booking(guest_name, room_num)
        if bookings:
            for booking in bookings:
                print(booking) # Print booking dictionary
        else:
            print("No bookings found matching your criteria.")

    elif choice == '5':
        booking_id = input("Enter booking ID to display details: ")
        hotel.display_booking_details(booking_id)

    elif choice == '6':
        break
    else:
        print("Invalid choice.")
