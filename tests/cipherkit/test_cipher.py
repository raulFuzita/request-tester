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
from app.cipherkit.cipher import CipherPy

class TestCipherPy(unittest.TestCase):

    def test_encryption_and_validation(self):
        cipher = CipherPy()
        data = "bdc2d631-a08c-410c-8d59-96add70aa5cd"
        encrypted_data = cipher.encrypt(data)

        validation_data = "bdc2d631-a08c-410c-8d59-96add70aa5cd"
        self.assertTrue(cipher.validate(encrypted_data, validation_data))

    def test_encryption_and_validation_with_custom_salt(self):
        cipher = CipherPy(salt="TEST")
        data = "bdc2d631-a08c-410c-8d59-96add70aa5cd"
        encrypted_data = cipher.encrypt(data)
        print(f"Encrypted data: {encrypted_data}")

        validation_data = "bdc2d631-a08c-410c-8d59-96add70aa5cd"
        self.assertTrue(cipher.validate(encrypted_data, validation_data))

if __name__ == '__main__':
    runner = CustomTestRunner()
    runner.log_failures = True
    runner.log_exceptions = True
    unittest.main(testRunner=runner)