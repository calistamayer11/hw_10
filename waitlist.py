import random
class Time:
    """A class that represents time in the format HH:MM"""
    def __init__(self, hour, minute):
        self.hour = int(hour)
        self.minute = int(minute)

    def __lt__(self, other):
        """Compare two times based on their hour and minute"""
        """ return True if self < other, and False otherwise"""
        if self.hour < other.hour:
            return True
        elif self.hour == other.hour and self.minute < other.minute:
            return True
        else:
            return False
    
    def __eq__(self, other):
        """Compare two times based on their hour and minute"""
        """ return True if self == other, and False otherwise"""
        if self.hour ==  other.hour and self.minute == other.minute:
            return True
        else:
            return False

    def __repr__(self):
        """Return the string representation of the time"""
        return f"{self.hour:02d}:{self.minute:02d}"

class Entry:
    """A class that represents a customer in the waitlist"""
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def __lt__(self, other):
        """Compare two customers based on their time, if equal then compare based on the customer name"""
        if self.time == other.time:
            return self.name < other.name
        return self.time < other.time
    

class Waitlist:
    def __init__(self):
        self._entries = []

    def add_customer(self, item, priority):
        #TODO add customers to the waiting list.
        pass

    def peek(self):
        #TODO peek and see the first customer in the waitlist (i.e., the customer with the highest priority).
        # Return a tuple of the extracted item (customer, time). Return None if the heap is empty
        pass

    def seat_customer(self):
        #TODO The program should extract the customer with the highest priority 
        # (i.e., the earliest reservation time) from the priority queue.
        # Return a tuple of the extracted item (customer, time)
        pass


    def print_reservation_list(self):
        #TODO Prints all customers in order of their priority (reservation time).
        #Maintain the heap property
        pass
    
    def change_reservation(self, name, new_priority):
        #TODO Change the reservation time (priority) for the customer with the given name
        pass

    #Add other methods you may need



