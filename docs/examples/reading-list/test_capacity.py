import unittest

from reading_list import can_add_book


class CapacityTests(unittest.TestCase):
    def test_default_boundary(self):
        self.assertTrue(can_add_book(19))
        self.assertFalse(can_add_book(20))
        self.assertFalse(can_add_book(21))

    def test_custom_and_zero_limits(self):
        self.assertTrue(can_add_book(2, 3))
        self.assertFalse(can_add_book(3, 3))
        self.assertFalse(can_add_book(0, 0))

    def test_negative_inputs(self):
        for count, limit in [(-1, 20), (0, -1)]:
            with self.subTest(count=count, limit=limit):
                with self.assertRaises(ValueError):
                    can_add_book(count, limit)


if __name__ == "__main__":
    unittest.main()
