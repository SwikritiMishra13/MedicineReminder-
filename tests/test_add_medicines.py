import unittest
from add_medicine import add_medicine

class TestAddMedicine(unittest.TestCase):

    def test_add_single_medicine(self):
        medicines = []
        add_medicine(medicines, "Paracetamol", "500mg", "10:00 AM")
        self.assertEqual(len(medicines), 1)
        self.assertEqual(medicines[0]["name"], "Paracetamol")

    def test_add_multiple_medicines(self):
        medicines = []
        add_medicine(medicines, "Med1", "10mg", "8 AM")
        add_medicine(medicines, "Med2", "20mg", "9 AM")
        self.assertEqual(len(medicines), 2)

if __name__ == "__main__":
    unittest.main()