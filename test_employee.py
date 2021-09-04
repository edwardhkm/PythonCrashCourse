import unittest
from Employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('ed', 'ho', 1000)

    def test_give_default_raise(self):
        salary = self.employee.give_raise()
        self.assertEqual(salary, 6000)

    def test_give_custom_raise(self):
        salary = self.employee.give_raise(1500)
        self.assertEqual(salary, 2500)

if __name__ == "__main__":
    unittest.main()
