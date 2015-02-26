"""
Takes the wunderground csv files and wrangles it for our needs.

The style guide follows the strict python PEP 8 guidelines.
@see http://www.python.org/dev/peps/pep-0008/

@author Aaron Zampaglione <azampaglione@g.harvard.edu>

@requires Python >=2.7
@copyright 2015
"""
import getopt
import os
import sys

import numpy as np
import pandas as pd

from datetime import datetime

#
# Constants
#

# String used to convert a string into a datetime object.
DATETIME_STR = "%Y/%m/%d"

# The number of days to look back for snow history.
SNOW_DAYS_HISTORY = 14


#
# Methods
#

def process(data, start, end):
    """
    Processes the dataframe and returns a wrangled
    data frame.

    This will fix the service times and make sure the the values are within
    the date range provided.

    Key arguments:
    data  -- The pandas dataframe (csv file).
    start -- The start datetime.
    end   -- The end datetime.
    """

    # Drop unecessary columns.
    data = data[[
        'date',
        'fog',
        'rain',
        'snow',
        'mintempi',
        'maxtempi',
        'meantempi',
        'precipi',
        'snowfalli',
        'meanwindspdi']]

    # Rename the columns for readability.
    data.columns = [
        'date',
        'fog',
        'rain',
        'snow',
        'temp_min',
        'temp_max',
        'temp_mean',
        'precip',
        'snow_fall',
        'wind_speed']

    data['date'] = pd.to_datetime(data['date'])

    data = data.apply(lambda row: add_rain_predict(data, row), axis=1)

    data = data.apply(lambda row: add_snow_predict(data, row), axis=1)
    data = data.apply(lambda row: add_snow_fall_predict(data, row), axis=1)
    data = data.apply(lambda row: add_snow_accum(data, row), axis=1)

    return data

def add_rain_predict(data, row):
    """
    Adds a rain prediction column to the desired row (day).

    Key arguments:
    data -- The entire data set.
    row  -- The current row.
    """

    row['rain_predict'] = get_predict_by_column(data, row, 'rain', 0)

    return row

def add_snow_accum(data, row):
    """
    Adds a snow accumulation column for the desired row (day).

    Key arguments:
    data -- The entire weather data set.
    row  -- The row we are manipulating.
    """
    
    # Find all of the necessary days in history.
    history = data[
        (data['date'] >= row['date'] - np.timedelta64(SNOW_DAYS_HISTORY, 'D')) & \
        (data['date'] < row['date'])]


    # Loop through each day in history and add the weighted snow fall
    #  for that historic day to the snow accumulation for the current day.
    snow_accum = 0.0
    for history_row in history.iterrows():
        # What is the day in history?
        day = history_row[1]['date']
        # How much snow fall for that day?
        snow_fall = history_row[1]['snow_fall']
        # The weight for the day is the 1/number of days ago
        weight = 1.0 / (row['date'] - day).days
        # Add the weighted snow fall to the current accumulation.
        snow_accum += snow_fall * weight

    # Add the current days snow fall to the mix and
    #  add the column to the row.
    row['snow_accum'] = round(snow_accum + row['snow_fall'], 1)

    return row

def add_snow_predict(data, row):
    """
    Adds a snow prediction column to the desired row (day).

    Key arguments:
    data -- The entire data set.
    row  -- The current row.
    """

    row['snow_predict'] = get_predict_by_column(data, row, 'snow', 0)

    return row

def add_snow_fall_predict(data, row):
    """
    Adds a snow fall prediction column to the desired row (day).

    Key arguments:
    data -- The entire data set.
    row  -- The current row.
    """

    row['snow_fall_predict'] = get_predict_by_column(data, row, 'snow_fall', 0.0)

    return row

def get_predict_by_column(data, row, column, default):
    """
    Returns the prediction for a desired column.

    Key arguments:
    data   -- The entire data set.
    row    -- The current row.
    column -- The desired column to get a prediction for.
    default -- The default value.
    """

    # Initialize todays prediction.
    prediction = default

    # Find the next days prediction
    tomorrow = data[
        data['date'] == (row['date'] + np.timedelta64(1, 'D'))
    ]

    # "Todays" prediction is just tomorrow's, if it exists.
    if (len(tomorrow) > 0):
        prediction = tomorrow.iloc[0][column]

    return prediction


#
# Trivial Methods
#


def main(args):
    """
    Main execution.

    Key arguments:
    args -- A dictionary of the arguments passed via command line.
    """

    # Convert the start and end dates to datetime objects.
    args['s'] = datetime.strptime(args['s'], DATETIME_STR)
    args['e'] = datetime.strptime(args['e'], DATETIME_STR)

    # Create a blank data frame.
    with open(args['i'], 'r') as file_handle:
        data = process(pd.read_csv(file_handle), args['s'], args['e'])

        # Save to disk.
        data.to_csv(args['o'], index=False)


def usage():
    """Prints the usage of the program."""

    print("\n" +
    "The following are arguments required:\n" +
    "\t-i: the input wunderground csv file.\n" +
    "\t-s: the (inclusive) start date (e.g. \"2015/01/01\").\n" +
    "\t-s: the (inclusive) end date (e.g. \"2015/01/31\").\n" +
    "\t-o: the output csv file.\n" +
    "\n" +
    "Example Usage:\n" +
    "\tpython weather-wrangle.py " + \
    "-i \"./wunderground.csv\" " + \
    "-s \"2015/01/01\" " + \
    "-e \"2015/01/31\" " + \
    "-o \"./weather.csv\"\n" +
    "\n")


"""Main execution."""
if __name__ == "__main__":

    # Determine command line arguments.
    try:
        rawargs, _ = getopt.getopt(sys.argv[1:], 'i:s:e:o:')
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    args = {}

    # Process each command line argument.
    for o, a in rawargs:
        args[o[1]] = a

    # The following arguments are required in all cases.
    for arg in ['i', 's', 'e', 'o']:
        if not arg in args:
            usage()
            sys.exit(2)

    main(args)
