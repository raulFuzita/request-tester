import sys
import os
# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Calculate the root directory by going up multiple levels
levels_up = 2  # Adjust this value based on your project structure
root_dir = os.path.abspath(os.path.join(script_dir, *([".."] * levels_up)))

# Add the root directory to sys.path
sys.path.append(root_dir)

# print("Modified sys.path:", sys.path)

import unittest
from app.util.unittest.custom_test_runner import CustomTestRunner
from app.idgenerator.sequence_id import SequentialIDGenerator

class TestSequentialIDGenerator(unittest.TestCase):

    def test_generate_id(self):
        generator = SequentialIDGenerator()
        id1 = generator.generate_id()
        id2 = generator.generate_id()
        self.assertEqual(id1, "1")
        self.assertEqual(id2, "2")

    def test_set_starting_id(self):
        generator = SequentialIDGenerator()
        generator.set_starting_id(10)
        id1 = generator.generate_id()
        id2 = generator.generate_id()
        self.assertEqual(id1, "11")
        self.assertEqual(id2, "12")

    def test_set_starting_id_negative(self):
        generator = SequentialIDGenerator()
        with self.assertRaises(ValueError):
            generator.set_starting_id(-1)

if __name__ == '__main__':
    runner = CustomTestRunner()
    runner.log_failures = True
    runner.log_exceptions = True
    unittest.main(testRunner=runner)
