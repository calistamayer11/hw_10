import unittest, sys, io
from waitlist import Waitlist


class TestWaitlist(unittest.TestCase):
    """Test the methods in WaitList"""

    def test_add_costumer(self):
        """Test the add_list method"""
        wl = Waitlist()
        self.assertEqual(len(wl), 0)
        wl.add_customer("Chris", "11:30")
        self.assertEqual(len(wl), 1)
        # Check if order holds when adding new customers
        wl.add_customer("Emily", "15:30")
        wl.add_customer("David", "07:05")
        self.assertEqual(len(wl), 3)
        self.assertEqual(str(wl._entries), "[Emily: 15:30, Chris: 11:30, David: 07:05]")
        # Check if order holds if the customers have the same time
        wl.add_customer("Calista", "18:35")
        wl.add_customer("Linda", "18:35")
        self.assertEqual(len(wl), 5)
        self.assertEqual(
            str(wl._entries),
            "[Linda: 18:35, Calista: 18:35, Emily: 15:30, Chris: 11:30, David: 07:05]",
        )

    def test_peek(self):
        """Test the peek method"""
        wl = Waitlist()
        wl.add_customer("Chris", "11:30")
        self.assertEqual(wl.peek(), ("Chris", "11:30"))
        wl.add_customer("Erin", "15:32")
        self.assertEqual(wl.peek(), ("Chris", "11:30"))
        wl.add_customer("Steven", "06:22")
        self.assertEqual(wl.peek(), ("Steven", "06:22"))

    def test_seat_customer(self):
        """Test the seat_customer method"""
        wl = Waitlist()
        wl.add_customer("Chris", "16:45")
        wl.add_customer("Erin", "20:50")
        wl.add_customer("Harry", "05:10")
        self.assertEqual(wl.seat_customer(), ("Harry", "05:10"))
        self.assertEqual(len(wl), 2)

    def test_change_reservation(self):
        """Test the change_reservation method"""
        wl = Waitlist()
        wl.add_customer("Chris", "12:45")
        # Check if it handles non existing customers
        self.assertTrue(wl.change_reservation("Chris", "12:30"))
        self.assertFalse(wl.change_reservation("Erin", "12:30"))
        self.assertEqual(wl.peek(), ("Chris", "12:30"))
        # Check if reordering is correct
        wl.add_customer("Harry", "15:15")
        wl.add_customer("Steven", "16:20")
        self.assertEqual(
            str(wl._entries), "[Steven: 16:20, Harry: 15:15, Chris: 12:30]"
        )
        wl.change_reservation("Steven", "14:15")
        self.assertEqual(
            str(wl._entries), "[Harry: 15:15, Steven: 14:15, Chris: 12:30]"
        )


unittest.main()
