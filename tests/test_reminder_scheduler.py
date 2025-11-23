import unittest
import inspect
from scheduler import start_reminder_loop

class TestScheduler(unittest.TestCase):

    def test_scheduler_function_exists(self):
        self.assertTrue(callable(start_reminder_loop))

    def test_scheduler_contains_loop(self):
        source = inspect.getsource(start_reminder_loop)
        self.assertIn("while True", source)

if __name__ == "__main__":
    unittest.main()