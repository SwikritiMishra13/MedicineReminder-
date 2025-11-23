import unittest
from tracker import add_medicine, mark_taken
from storage import load_data, save_data

class TestMarkTaken(unittest.TestCase):

    def setUp(self):
        save_data({"medicines": []})

    def test_mark_medicine_taken(self):
        add_medicine("Paracetamol", "500mg", "10:00 AM")
        mark_taken(0)
        data = load_data()
        self.assertEqual(data["medicines"][0]["status"], "taken")

if __name__ == "__main__":
    unittest.main()