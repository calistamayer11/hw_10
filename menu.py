from waitlist import Waitlist


class Menu:
    """This class represents the menu"""

    def __init__(self):
        """Initialise the menu class"""
        self.waitlist = Waitlist()

    def _check_valid_format(self, time):
        """Check if the time is valid"""
        for i in range(len(time)):
            if i == 2:
                continue
            if time[i].isdigit() != True:
                return False

        if (
            len(time) != 5
            or int(time[0]) > 2
            or (int(time[0]) == 2 and int(time[1]) > 3)
            or time[2] != ":"
            or int(time[3]) > 5
        ):
            return False
        return True

    def run(self):
        """prints the menu"""
        print("Welcome to the Restaurant Reservation System!")
        print("==============================================")
        print("Please select an option:")
        print("1. Add a customer to the waitlist")
        print("2. Seat the next customer")
        print("3. Change the time of a customer's reservation")
        print("4. Peek at the next customer")
        print("5. Print the reservation list")
        print("6. Quit")
        print("")
        while True:

            choice = input("Enter your choice (1-6): ")
            print("*************************************************")
            # Each one of these options should call a method from Waitlist class
            if choice == "1":
                # TODO """Add a customer to the waitlist"""
                print("Enter the customer's name:")
                name = input()
                while True:
                    print("Enter the time of the reservation (HH:MM):")
                    time = input()
                    if self._check_valid_format(time):
                        break
                    print("Please enter with the format HH:MM")
                self.waitlist.add_customer(name, time)
                print(name + " has been added to the waitlist at " + time)

            elif choice == "2":
                # TODO"""Seat the next customer"""
                seated_customer = self.waitlist.seat_customer()
                if seated_customer is None:
                    print("There are no customers in the waitlist")
                else:
                    print(
                        f"\nSeated customer: {seated_customer(0)}, reservation time: {seated_customer(1)}\n"
                    )

            elif choice == "3":
                # TODO"""Change the time of a customer's reservation"""
                name = input("Enter the customer's name:")
                while True:
                    updated_time = input(
                        "Enter the new time of the reservation (HH:MM):"
                    )
                    if self._check_valid_format(updated_time):
                        break
                    print("Please enter with the format HH:MM")
                change_reservation = self.waitlist.change_reservation(
                    name, updated_time
                )
                if change_reservation:
                    print(
                        f"\n{name}'s reservation time has been changed to {updated_time}\n"
                    )
                else:
                    print(
                        "There is no record of that name. Please try to make a new reservation!"
                    )

            elif choice == "4":
                # TODO"""Peek at the next customer"""
                next_customer = self.waitlist.peek()
                if next_customer is None:
                    print("There are no customers in the waitlist")
                else:
                    print(
                        f"The next customer on the waitlist is: {next_customer(0)}, reservation time: {next_customer(1)}"
                    )

            elif choice == "5":
                # TODO"""Print the waitlist"""
                self.waitlist.print_reservation_list()

            elif choice == "6":
                """exit the program at any time"""
                print("Thank you for using the Restaurant Reservation System!")
                break
            else:
                print("Invalid choice. Try again.")


s = Menu()
s.run()
