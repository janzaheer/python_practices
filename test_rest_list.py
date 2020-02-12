import unittest
import os
import sys

from rest_list import get_open_restaurants

file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)


class TestInputDayTime(unittest.TestCase):
    def test_input_correct_values(self):
        input_day_time = 'Sun 10am'
        input_csv_filename = 'rest_hours.csv'
        self.assertTrue(True, get_open_restaurants(
            csv_filename=input_csv_filename, day_time=input_day_time))

    def test_input_incorrect_day_value(self):
        input_day_time = 'Sund 10am'
        input_csv_filename = 'rest_hours.csv'
        with self.assertRaises(AssertionError):
            get_open_restaurants(
                csv_filename=input_csv_filename, day_time=input_day_time)

    def test_input_incorrect_time_value(self):
        input_day_time = 'Sun 10cm'
        input_csv_filename = 'rest_hours.csv'

        with self.assertRaises(AssertionError):
            get_open_restaurants(
                csv_filename=input_csv_filename, day_time=input_day_time)


class TestInputCSVFilename(unittest.TestCase):
    def test_input_correct_filename(self):
        input_day_time = 'Sun 10am'
        input_csv_filename = 'rest_hours.csv'
        self.assertTrue(True, get_open_restaurants(
            csv_filename=input_csv_filename, day_time=input_day_time))

    def test_input_incorrect_filename(self):
        input_day_time = 'Sun 10am'
        input_csv_filename = 'rest_hour.csv'
        with self.assertRaises(AssertionError):
            get_open_restaurants(
                csv_filename=input_csv_filename, day_time=input_day_time)

    def test_input_reversed_column_csv(self):
        input_day_time = 'Sun 10am'
        input_csv_filename = 'reversed_column_rest_hours.csv'
        with self.assertRaises(AssertionError):
            get_open_restaurants(
                csv_filename=input_csv_filename, day_time=input_day_time)


if __name__ == '__main__':
    unittest.main()
