import unittest
import HtmlTestRunner
from configs.config import PATH_TO_HTML_REPORT
from utils.time_utils import current_date


def run_test_in_multiple_module_file_generate_html_report():
    # Create test suite.
    test_suite = unittest.TestSuite()
    # Load all test case class in current folder.
    all_test_cases = unittest.defaultTestLoader.discover('tests', 'test_*.py')
    # Loop the found test cases and add them into test suite.
    for test_case in all_test_cases:
        test_suite.addTests(test_case)

    # Create HtmlTestRunner object and run the test suite.
    test_runner = HtmlTestRunner.HTMLTestRunner(output=PATH_TO_HTML_REPORT.format(cob_date=current_date()))
    test_runner.run(test_suite)


if __name__ == '__main__':
    run_test_in_multiple_module_file_generate_html_report()
