import unittest
import requests
import json
from utils.time_utils import *
from configs.config import *
from configs.DateMax import *
from core.json_parser import JsonParser


class DateMaxField(unittest.TestCase):
    @staticmethod
    def test_exclude_data_later_than_1_day():
        # Open URL with prepared params and get content from response
        html_text = requests.get(PATH_TO_API, params=date_max_plus_1_day).content

        # Read JSON file and parse object by mapping
        data_object = JsonParser(json.loads(html_text))

        # Check that in response no data later than 1 day
        for row in data_object.data:
            assert row[3] >= date_abbr_month_and_time_minus_day()

    def test_date_not_be_greater_than_100_years(self):
        # Open URL with prepared params and get content from response
        html_text = requests.get(PATH_TO_API, params=date_max_plus_100_years).content

        # Read JSON file and parse object by mapping
        data_object = JsonParser(json.loads(html_text))

        # Check that in response last date equal + 100 years
        self.assertEqual(data_object.data[-1][3][:11], date_abbr_month_plus_100_years())

    def test_static_date(self):
        # Open URL with prepared params and get content from response
        html_text = requests.get(PATH_TO_API, params=static_date).content

        # Read JSON file and parse object by mapping
        data_object = JsonParser(json.loads(html_text))

        self.assertEqual(data_object.data[-1][3][:11], current_date())

    def test_error_message_for_date_more_than_100_years(self):
        expected_result = 'invalid value specified for query parameter \'date-max\': relative days must not be greater than 100 years (36525 days)'
        # Open URL with prepared params and get content from response
        html_text = requests.get(PATH_TO_API, params=date_more_than_100_years).content

        # Read JSON file and parse object by mapping
        data_object = JsonParser(json.loads(html_text))

        # Check error message
        self.assertEqual(data_object.message, expected_result)

    def test_error_code_for_date_more_than_100_years(self):
        expected_result = '400'
        # Open URL with prepared params and get content from response
        html_text = requests.get(PATH_TO_API, params=date_more_than_100_years).content

        # Read JSON file and parse object by mapping
        data_object = JsonParser(json.loads(html_text))

        # Check error code
        self.assertEqual(data_object.code, expected_result)

    def test_error_message_for_wrong_static_date(self):
        expected_result = 'invalid value specified for query parameter \'date-max\': invalid datetime specified (expected \'YYYY-MM-DD\', \'YYYY-MM-DDThh:mm:ss\', \'YYYY-MM-DD_hh:mm:ss\' or \'YYYY-MM-DD hh:mm:ss\')'
        # Open URL with prepared params and get content from response
        html_text = requests.get(PATH_TO_API, params=wrong_static_date).content

        # Read JSON file and parse object by mapping
        data_object = JsonParser(json.loads(html_text))

        # Check error message
        self.assertEqual(data_object.message, expected_result)

    def test_error_code_for_for_wrong_static_date(self):
        expected_result = '400'
        # Open URL with prepared params and get content from response
        html_text = requests.get(PATH_TO_API, params=wrong_static_date).content

        # Read JSON file and parse object by mapping
        data_object = JsonParser(json.loads(html_text))

        # Check error code
        self.assertEqual(data_object.code, expected_result)

    def test_error_message_for_empty_static_date(self):
        expected_result = 'invalid value specified for query parameter \'date-max\': invalid datetime specified (expected \'YYYY-MM-DD\', \'YYYY-MM-DDThh:mm:ss\', \'YYYY-MM-DD_hh:mm:ss\' or \'YYYY-MM-DD hh:mm:ss\')'
        # Open URL with prepared params and get content from response
        html_text = requests.get(PATH_TO_API, params=empty_static_date).content

        # Read JSON file and parse object by mapping
        data_object = JsonParser(json.loads(html_text))

        # Check error message
        self.assertEqual(data_object.message, expected_result)

    def test_error_code_for_empty_static_date(self):
        expected_result = '400'
        # Open URL with prepared params and get content from response
        html_text = requests.get(PATH_TO_API, params=empty_static_date).content

        # Read JSON file and parse object by mapping
        data_object = JsonParser(json.loads(html_text))

        # Check error code
        self.assertEqual(data_object.code, expected_result)

    def test_wrong_message_for_integer_date(self):
        expected_result = 'invalid value specified for query parameter \'date-max\': invalid datetime specified (expected \'YYYY-MM-DD\', \'YYYY-MM-DDThh:mm:ss\', \'YYYY-MM-DD_hh:mm:ss\' or \'YYYY-MM-DD hh:mm:ss\')'
        # Open URL with prepared params and get content from response
        html_text = requests.get(PATH_TO_API, params=integer_value).content

        # Read JSON file and parse object by mapping
        data_object = JsonParser(json.loads(html_text))

        # Check error message
        self.assertEqual(data_object.message, expected_result)

    def test_error_code_for_integer_date(self):
        expected_result = '400'
        # Open URL with prepared params and get content from response
        html_text = requests.get(PATH_TO_API, params=integer_value).content

        # Read JSON file and parse object by mapping
        data_object = JsonParser(json.loads(html_text))

        # Check error code
        self.assertEqual(data_object.code, expected_result)

    def test_error_message_for_double_values(self):
        expected_result = 'parameter \'date-max\' specified more than once'
        # Open URL with prepared params and get content from response
        html_text = requests.get(PATH_TO_API, params=double_date_max).content

        # Read JSON file and parse object by mapping
        data_object = JsonParser(json.loads(html_text))

        # Check error message
        self.assertEqual(data_object.message, expected_result)

    def test_error_code_for_double_values(self):
        expected_result = '400'
        # Open URL with prepared params and get content from response
        html_text = requests.get(PATH_TO_API, params=double_date_max).content

        # Read JSON file and parse object by mapping
        data_object = JsonParser(json.loads(html_text))

        # Check error code
        self.assertEqual(data_object.code, expected_result)

