import datetime
import csv


CSV_FILENAME = 'rest_hours.csv'

WEEK_DAYS_DICTS = {'mon': 1, 'tue': 2, 'wed': 3, 'thu': 4, 'fri': 5, 'sat': 6, 'sun': 7}
WEEK_DAYS_DICTS_MAP = {1: 'mon', 2: 'tue', 3: 'wed', 4: 'thu', 5: 'fri', 6: 'sat', 7: 'sun'}

MULTIPLE_SCHEDULES_SEPARATOR = '/'

INPUT_VALIDATION_TEXT = (
    "Input day time format is not correct please try again by "
    "giving the correct format."
)


def read_restaurant_csv(csv_filename):
    """
    This function reads the CSV file and returns its object,
    Note: We can directly iterate CSV file reader object as the object
    contains the list of data
    :return: CSV file reader object
    """
    try:
        csv_file_reader = csv.reader(open(csv_filename), delimiter=',')
    except IOError:
        raise AssertionError(
            'CSV Filename is not correct, please try again'
            ' with the correct file name.'
        )
    return csv_file_reader


def format_str_to_time_obj(time_value):
    """
    The function is used to convert the time of user_input and restaurant's
    open and close time  in datetime object, and returns the formatted value
    :param time_value: 10am or etc
    :return: formatted datetime value
    """
    try:
        if ':' in time_value:
            formatted_value = datetime.datetime.strptime(
                time_value, '%I:%M%p'
            )
        else:
            formatted_value = datetime.datetime.strptime(
                time_value, '%I%p'
            )
    except ValueError:
        raise AssertionError(INPUT_VALIDATION_TEXT)

    return formatted_value


def get_days_with_open_and_close_time(day_open_close_string):
    """
    The function is used break the time range string into open_close_time
    and days, time range would be like (Mon-Sun 11:30 am - 9:30 pm)
    :param day_open_close_string:
    :return: open_close_time and days
    """

    # removes all spaces from the string (Mon-Sun 11:30 am - 9:30 pm)
    day_open_close_string = day_open_close_string.replace(' ', '').lower()
    character_array = list(day_open_close_string)
    open_close_time = None
    days = None
    for index, value in reversed(list(enumerate(character_array))):
        # check and break the loop if pointer reached to minimum 3rd last
        # index of the list to avoid code breakage
        if index - 3 == 0:
            break
        # get the last three element from where the pointer
        # exits and join the list into string
        day = ''.join(character_array[index - 2:index + 1])

        # Condition check either the day we get matches the week days,
        # If True then this code break the day and time part separately
        # and break the loop.
        if WEEK_DAYS_DICTS.get(day):
            open_close_time = ''.join(character_array[index + 1:])
            days = ''.join(character_array[0:index + 1])
            break
    return open_close_time, days


def verify_time_operation(open_time, close_time, input_format):
    """
    This function verify the time period that user enters exits between the
    restaurant starting and ending, if yes it returns True else False
    :param open_time:
    :param close_time:
    :param input_format:
    :return:
    """
    open_time_datetime = format_str_to_time_obj(open_time)
    close_time_datetime = format_str_to_time_obj(close_time)
    input_time = format_str_to_time_obj(input_format)

    # Condition is used to check while restaurant closes on other day,
    # if yes then the code is used to add 1 day in close_time_datetime
    # and input_time to get the perfect time accordingly
    if 'am' in close_time:
        close_time_datetime = close_time_datetime + datetime.timedelta(days=1)
        input_time = input_time + datetime.timedelta(days=1)
    if open_time_datetime <= input_time <= close_time_datetime:
        return True

    return False


def check_input_time_within_operational_hours(open_close_time, days, input_format):
    """
    The function is used to convert the values according to need and checks
    while user input time exits in starting and ending time of restaurant
    :param open_close_time: ['9am', '11pm']
    :param days: ['Mon-Thu', 'Sun']
    :param input_format: ['Mon', '9am']
    :return: Boolean
    """
    if open_close_time:
        open_close_times = open_close_time.split('-')
    else:
        return False
    if len(open_close_times) != 2:
        return False
    open_time = open_close_times[0]
    close_time = open_close_times[1]
    days_list = days.split(',')
    for day_data in days_list:
        days = day_data.split('-')
        if len(days) == 1:
            return verify_time_operation(
                open_time, close_time, input_format[1])

        elif len(days) == 2:
            start_day = days[0]
            end_day = days[1]
            for i in range(WEEK_DAYS_DICTS.get(start_day), WEEK_DAYS_DICTS.get(end_day) + 1):
                if WEEK_DAYS_DICTS_MAP.get(i) and input_format[0] == WEEK_DAYS_DICTS_MAP.get(i):
                    return verify_time_operation(
                        open_time, close_time, input_format[1]
                    )
    return False


def restaurant_is_operational_within_input(restaurant_csv_data, input_format):
    """
    The function print the restaurant name after verifying the user input
    day and time
    """
    for rows in restaurant_csv_data:
        if all(x in rows[0] for x in ['am', 'pm', '-']):
            raise AssertionError(
                "CSV File, first row should be restaurant names and"
                " second column should be day time ranges")

        separated_schedules = rows[1].split(MULTIPLE_SCHEDULES_SEPARATOR)
        if not separated_schedules:
            continue
        for separated_schedule in separated_schedules:
            open_close_time, days = get_days_with_open_and_close_time(separated_schedule)
            if open_close_time and days and \
                    check_input_time_within_operational_hours(
                        open_close_time, days, input_format):
                    print(rows[0])


def validate_input_data(data):
    # input_data[0] is the day(Mon) coming from input,
    # Its validate if week day enters wrong in input
    if data[0] not in [val for key, val in WEEK_DAYS_DICTS_MAP.items()]:
        raise AssertionError(INPUT_VALIDATION_TEXT)

    # validates if input data split not equal to 2
    if not len(data) == 2:
        raise AssertionError(INPUT_VALIDATION_TEXT)

    return True


def get_open_restaurants(csv_filename, day_time):
    # Split User Input to get day and time separately from user input
    data = day_time.lower().split(' ')

    # Validates the input user data
    validate_input_data(data)

    # read CSV file
    restaurant_csv_data = read_restaurant_csv(csv_filename)

    # Check and list down all the restaurants are operational/open
    # in time frame provided by user in user input
    restaurant_is_operational_within_input(restaurant_csv_data, data)


if __name__ == "__main__":
    INPUT_CSV_FILENAME = raw_input("Enter csv filename: ")
    INPUT_FROM_USER = raw_input(
        "Enter Day and Open Time to Check Restaurant"
        " Status e.g: (Mon 10am) "
    )
    get_open_restaurants(
        csv_filename=INPUT_CSV_FILENAME, day_time=INPUT_FROM_USER
    )
