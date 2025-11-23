import unittest
from view_medicines import view_medicines

class TestViewMedicines(unittest.TestCase):

    def test_empty_list(self):
        medicines = []
        output = view_medicines(medicines)
        self.assertEqual(output, [])

    def test_non_empty_list(self):
        medicines = [
            {"name": "Paracetamol", "dose": "500mg", "time": "10 AM"}
        ]
        output = view_medicines(medicines)
        self.assertEqual(len(output), 1)

if _name_ == "_main_":
    unittest.main()