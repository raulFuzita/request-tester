import sys
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

levels_up = 2
root_dir = os.path.abspath(os.path.join(script_dir, *([".."] * levels_up)))
sys.path.append(root_dir)

import unittest
from app.util.unittest.custom_test_runner import CustomTestRunner
from app.dbconnector.db_connection_factory import DatabaseConnectionManagerFactory

class TestDataConnectionManagerFactory(unittest.TestCase):

    def test_get_instance(self):
        db_url = "sqlite://"
        db_manager = DatabaseConnectionManagerFactory.get_instance(db_url)
        self.assertIsNotNone(db_manager)
        self.assertEqual(db_manager.id, db_manager.id)

    def test_get_instance_multiple(self):
        db_url = "sqlite://"
        db_manager = DatabaseConnectionManagerFactory.get_instance(db_url)
        db_manager2 = DatabaseConnectionManagerFactory.get_instance(db_url)
        self.assertIsNotNone(db_manager)
        self.assertIsNotNone(db_manager2)
        self.assertEqual(db_manager.id, db_manager2.id)

if __name__ == '__main__':
    runner = CustomTestRunner()
    runner.log_failures = True
    runner.log_exceptions = True
    unittest.main(testRunner=runner)