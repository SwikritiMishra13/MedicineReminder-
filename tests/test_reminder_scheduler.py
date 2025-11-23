import unittest
from scheduler import start_scheduler

class TestScheduler(unittest.TestCase):

    def test_scheduler_runs(self):
        try:
            start_scheduler([])
            ran = True
        except:
            ran = False

        self.assertTrue(ran)

if _name_ == "_main_":
    unittest.main()