import unittest
import traceback
import os
import time
from dotenv import load_dotenv

load_dotenv()

class CustomTestResult(unittest.TextTestResult):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log_failures = False
        self.log_exceptions = False
    
    def addFailure(self, test, err):
        super().addFailure(test, err)
        if self.log_failures:
            self._log_error(test, err)

    def addError(self, test, err):
        super().addError(test, err)
        if self.log_exceptions:
            self._log_error(test, err)

    def _log_error(self, test, err):
        test_name = self.getDescription(test)
        error_message = str(err[1])
        tb_formatted = traceback.format_tb(err[1].__traceback__)
        currentTime = time.strftime("%Y-%m-%d\t%H:%M:%S")
        full_error_message = f"[{currentTime}] Test {test_name} failed with error:\n{error_message}\nTraceback:\n{''.join(tb_formatted)}"

        log_dir = os.getenv("LOG_DIR_TESTS")
        if log_dir:
            os.makedirs(log_dir, exist_ok=True)
            log_filename = os.path.join(log_dir, "test_failures.log")
        else:
            log_filename = "test_failures.log"

        # Check if the log file exists and is larger than 1MB
        if os.path.exists(log_filename) and os.path.getsize(log_filename) > 1024 * 1024:
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            log_filename = os.path.join(log_dir, f"test_failures_{timestamp}.log")

        with open(log_filename, "a") as logfile:
            logfile.write(full_error_message + "\n")