import unittest
from storage import load_data, save_data

class TestStorage(unittest.TestCase):

    def test_save_and_load(self):
        sample = {"medicines": [{"name": "Test", "dosage": "10mg", "time": "9:00 AM"}]}
        save_data(sample)
        loaded = load_data()
        self.assertEqual(sample, loaded)

if __name__ == "__main__":
    unittest.main()