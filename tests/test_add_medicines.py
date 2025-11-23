import unittest
import json
import os

from src.tracker import add_medicine
from src.storage import load_medicines, save_medicines

class TestAddMedicine(unittest.TestCase):

    def setUp(self):
        # Clear medicines.json before each test
        self.test_file = "src/data/medicines.json"
        with open(self.test_file, "w") as f:
            f.write("[]")  # empty list

    def test_add_single_medicine(self):
        add_medicine("Paracetamol", "500mg", "10:00 AM")
        
        medicines = load_medicines()
        self.assertEqual(len(medicines), 1)
        self.assertEqual(medicines[0]["name"], "Paracetamol")

    def test_add_multiple_medicines(self):
        add_medicine("Med1", "10mg", "8 AM")
        add_medicine("Med2", "20mg", "9 AM")

        medicines = load_medicines()
        self.assertEqual(len(medicines), 2)

if _name_ == "_main_":
    unittest.main()