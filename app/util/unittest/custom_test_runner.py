import unittest
from .custom_test_result import CustomTestResult

class CustomTestRunner(unittest.TextTestRunner):
    resultclass = CustomTestResult

    def _makeResult(self):
        result = self.resultclass(self.stream, self.descriptions, self.verbosity)
        result.log_failures = getattr(self, 'log_failures', False)
        result.log_exceptions = getattr(self, 'log_exceptions', False)
        return result