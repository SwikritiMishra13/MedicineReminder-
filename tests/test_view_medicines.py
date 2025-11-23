import unittest
from tracker import show_all_medicines
from storage import save_data

class TestViewMedicines(unittest.TestCase):

    def test_view_medicines(self):
        save_data({"medicines": []})  # ensure file exists
        try:
            show_all_medicines()
            ran = True
        except:
            ran = False
        self.assertTrue(ran)

if __name__ == "__main__":
    unittest.main()