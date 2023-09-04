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
from app.commands.init_required_tables import RequiredTablesCommand

class TestRequiredTablesCommand(unittest.TestCase):

    def test_required_tables_command(self):
        requiredTablesCommand = RequiredTablesCommand()
        self.assertTrue(requiredTablesCommand.execute())


if __name__ == '__main__':
    runner = CustomTestRunner()
    runner.log_failures = True
    runner.log_exceptions = True
    unittest.main(testRunner=runner)