import csv
from datetime import datetime  # Import the datetime module


DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"
def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string containing the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"



def convert_date(iso_string):  # line 2
    """Converts an ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    # date_object = datetime.fromisoformat(iso_string)  # Convert string to datetime using strptime # line 10
    date_object = datetime.fromisoformat(iso_string)
    human_readable_date = date_object.strftime('%A %d %B %Y')  # Format date
    return human_readable_date  # Return the formatted date

# Test the function:
result = convert_date("2021-07-05T07:00:00+08:00")  # Call the function and store the result
print(f"{result}")  # Print the result to see the output # line 15
        # expected_result = "Monday 05 July 2021"

def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    pass


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value. 
    """
    
    if len(weather_data) == 0:  # Check if the list is empty
        return "list is empty, cannot divide by zero"
    
    # Check if all elements are numbers
    numeric_data = []
    for item in weather_data:
        try:
            numeric_data.append(float(item))  # Convert items to float
        except (ValueError, TypeError):
            return "All items in the list must be numbers"  # Error if an item is not a number

    # Calculate mean: sum of numbers divided by the count of numbers
    return sum(numeric_data) / len(numeric_data)  # Return mean of numeric data
    
   
# test the function:
  # Call the function and store the result
my_mean = calculate_mean([45, 36, 38, 74, 99, 100, 101, 102, 103, 104])
print(f'the mean is:{my_mean}')
    
  
   
    


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    pass


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    pass


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    pass


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    
