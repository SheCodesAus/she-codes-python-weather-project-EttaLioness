import csv
import statistics
from datetime import datetime
from typing import Any

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts an ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    # Method: .fromisoformat(parameter=date_string_in ISO format – yyyy-mm-dd) from the date class 
    #of Python datetime module; constructs a date object from a string containing date in ISO format. i.e., yyyy-mm-dd
    #refence: https://pythontic.com/datetime/date/fromisoformat

    #The strftime() function is used to convert date and time objects to their string
    #representation reference: https://www.geeksforgeeks.org/python-strftime-function/?ref=gcse
    date = datetime.fromisoformat(iso_string)
    return date.strftime("%A %d %B %Y")


def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.
    
    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    temp_in_celcius = (float(temp_in_farenheit) - 32) * (5/9)
    return round(temp_in_celcius, 1) #roundes down to one decimal place: round(variable,number of dp)

def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    #map() loops through data & runs a function on each item , syntax: map(function, iterables)
    newList = (map(float, weather_data))
    #to use .mean import statistics package
    mean = statistics.mean(newList)
    return mean

def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    weather_data = []
    with open(csv_file) as csv_file: # opens all csv from root directory
        reader = csv.reader(csv_file)
        next(reader) #skip the first (title) line in the code

        #skip blank rows & add to list
        for line in reader:
            if len(line) > 0 :
                weather_data.append([line[0], int(line[1]), int(line[2])])  
    return weather_data


#Or could do this
# def load_data_from_csv(csv_file):
#     weather_data=[]
#     with open(csv_file) as csv_file:
#         csv_reader = csv.reader(csv_file)
#         next(csv_reader)
#         # csv_reader=list(csv_reader)
#         print(csv_reader)
#         for row in csv_reader:
#             if row == []:
#                 continue
#             weather_data.append([row[0], float(row[1]),float(row[2])])
#     return weather_data

def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    if weather_data == []:
        return ()
    else:
        minLocation = 0
        minTemp = weather_data[0]
        index = 0
        for num in weather_data:
            if float(num) <= float(minTemp):
                minTemp = float(num)
                minLocation = index
            index +=1
        return minTemp, minLocation


# ##0r do this
#     if weather_data == []:
#         return ()
#     min_value = weather_data[0]
#     min_index = 0
#     for val in range(len(weather_data)):
#         if weather_data[val] <= min_value:
#             min_value = weather_data[val]
#             min_index = val
#         # display the min value and index
#         # print(min_value)
#         # print(min_index)
#     results = (float(min_value) , min_index)
#     print(type(results))
#     return results

def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if weather_data == []:
        return ()
    else:
        maxLocation = 0
        max_temp = weather_data[0]
        index = 0
        for num in weather_data:
            if float(num) >= float(max_temp):
                max_temp = float(num)
                maxLocation = index
            index +=1
        return max_temp, maxLocation


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    #establish variables & creating new lists by looping
    numberOfDays = str(len(weather_data))
    summary = ""

    # Generating new lists for dates, min & max from weather_date list indexes
    datesList = [date[0] for date in weather_data]
    minTempList = [min[1] for min in weather_data]  #https://www.delftstack.com/howto/python/one-line-for-loop-python/
    maxTempList = [max[2] for max in weather_data]


    minTemp =  format_temperature(convert_f_to_c(find_min(minTempList)[0]))
    maxTemp = format_temperature(convert_f_to_c(find_max(maxTempList)[0]))
    minDate = convert_date(datesList[find_min(minTempList)[1]])
    maxDate = convert_date(datesList[find_max(maxTempList)[1]])

    # Calculating Average min & max
    avgMin = format_temperature(convert_f_to_c(calculate_mean(minTempList)))
    avgMax = format_temperature(convert_f_to_c(calculate_mean(maxTempList)))


    # print(f" lowest_temp: {minTemp}")
    # print(f" highest_temp: {maxTemp}")
    # print(f" avg low: {avgMin}")
    # print(f" avg high: {avgMax}")

    summary += f"{numberOfDays} Day Overview\n  The lowest temperature will be {minTemp}, and will occur on {minDate}.\n  The highest temperature will be {maxTemp}, and will occur on {maxDate}.\n  The average low this week is {avgMin}.\n  The average high this week is {avgMax}.\n"
    return summary
# print(generate_summary(weather_data = load_data_from_csv("tests/data/example_two.csv")))


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary = ''
    for line in weather_data:
        summary += f"---- {convert_date(line[0])} ----\n  Minimum Temperature: {format_temperature(convert_f_to_c(line[1]))}\n  Maximum Temperature: {format_temperature(convert_f_to_c(line[2]))}\n\n"
    return(summary)

    #==========another way==========
    # daily_summary = ''
    # for day in weather_data:
    #     date  = f'---- {convert_date(day[0])} ----\n'
    #     minTemp = f'  Minimum Temperature: {format_temperature(convert_f_to_c(day[1]))}\n'
    #     maxTemp = f'  Maximum Temperature: {format_temperature(convert_f_to_c(day[2]))}\n'
    #     daily_summary += date + minTemp + maxTemp + '\n'
    # return daily_summary
