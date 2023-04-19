import random


class Time:
    """Class that represents the time of a reservation"""

    def __init__(self, hour, minute):
        self.hour = int(hour)
        self.minute = int(minute)

    def __lt__(self, other):
        """return True if self < other, and False otherwise"""
        if self.hour < other.hour:
            return True
        elif self.hour == other.hour and self.minute < other.minute:
            return True
        else:
            return False

    def __eq__(self, other):
        """Compare two times based on their hour and minute"""
        """return True if self == other, and False otherwise"""
        if self.hour == other.hour and self.minute == other.minute:
            return True
        else:
            return False

    def __repr__(self):
        """The string representation of the time"""
        return f"{self.hour:02d}:{self.minute:02d}"


class Entry:
    """A class that represents a customer and their reservation time"""

    def __init__(self, name, time):
        self.name = name
        self.time = time

    def __lt__(self, other):
        """Less than operator"""
        if self.time == other.time:
            return self.name < other.name
        return self.time < other.time

    def __repr__(self):
        """The string representation of the custome and their reservation time"""
        return f"{self.name}: {self.time}"


class Waitlist:
    def __init__(self):
        self._entries = []

    def __len__(self):
        return len(self._entries)

    def add_customer(self, item, priority):
        # TODO add customers to the waiting list.
        customer = Entry(item, priority)
        if len(self._entries) == 0 or self._entries[-1] > customer:
            self._entries.append(customer)

        else:
            for i in range(len(self._entries)):
                if self._entries[i] > customer:
                    continue
                self._rearrange(customer, i)
                break

    def _rearrange(self, customer, index):
        """Rearranges the priority queue so that the customer with the highest priority is at the front of"""
        new_entries = self._entries[:index]
        new_entries.append(customer)
        new_entries += self._entries[index:]
        self._entries = new_entries

    def peek(self):
        """returns tuple of customer and time"""
        # TODO peek and see the first customer in the waitlist (i.e., the customer with the highest priority).
        if len(self._entries) == 0:
            return None
        else:
            return (self._entries[-1].name, self._entries[-1].time)

    def seat_customer(self):
        """Returns a tuple of customer and time of the customer"""
        # TODO The program should extract the customer with the highest priority
        if len(self._entries) == 0:
            return None
        else:
            last_seated_customer = (self._entries[-1].name, self._entries[-1].time)
            self._entries.pop()
            return last_seated_customer

    def print_reservation_list(self):
        """prints the reservation list"""
        # TODO Prints all customers in order of their priority (reservation time).
        print("__________________________________________________")
        for i in range(len(self._entries)):
            index = len(self._entries) - i - 1
            entry = self._entries[index]
            print(
                "The next customer on the waitlist is: "
                + entry.name
                + ", time: "
                + entry.time
            )
        print("__________________________________________________")

    def change_reservation(self, name, new_priority):
        """changes the reservatioon time (priority) for the customer with the given name"""
        # TODO Change the reservation time (priority) for the customer with the given name
        for i in range(len(self._entries)):
            if self._entries[i].name == name:
                self._entries.remove(self._entries[i])
                self.add_customer(name, new_priority)
                return True
        return False

    # Add other methods you may need
