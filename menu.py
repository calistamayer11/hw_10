from waitlist import Waitlist
class Menu:
    """A class representing the menu for the restaurant reservation program"""

    def __init__(self):
        """Initialize the menu with the waitlist object"""
        self.waitlist = Waitlist()

    def run(self):
        """Print the main menu"""
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
            #Each one of these options should call a method from Waitlist class 
            if choice == "1":
                #TODO """Add a customer to the waitlist"""
                pass

            elif choice == "2":
                #TODO"""Seat the next customer"""
                pass

            elif choice == "3":
                #TODO"""Change the time of a customer's reservation"""
                pass

            elif choice == "4":
                #TODO"""Peek at the next customer"""
                pass

            elif choice == "5":
                #TODO"""Print the waitlist"""
                pass
            elif choice == "6":
                """exit the program at any time"""
                print("Thank you for using the Restaurant Reservation System!")
                break
            else:
                print("Invalid choice. Try again.")
    

s = Menu()
s.run()

