"""
Adds additional weather features to a data set.

The style guide follows the strict python PEP 8 guidelines.
@see http://www.python.org/dev/peps/pep-0008/

@author Aaron Zampaglione <azampaglione@g.harvard.edu>

@requires Python >=2.7
@copyright 2015
"""
import numpy as np
import pandas as pd


#
# Consts
#


# The name of the datetime column.
DATE_COL = 'service_day'

# The number of days to look back for snow history.
SNOW_DAYS_HISTORY = 14


#
# Methods.
#

def init(data):
    """
    Initializes the current columns to the proper data type(s).

    Key arguments:
    data -- The current dataframe.
    """

    # Convert the date fields.
    data[DATE_COL] = pd.to_datetime(data[DATE_COL])

    # Convert the bool fields.
    bools = ['fog', 'hail', 'rain', 'snow']

    data[bools] = data[bools].astype(int)

    # Convert the floating fields.
    floats = ['temp_min', 'temp_max', 'temp_mean',
        'rain_fall', 'snow_fall', 'wind_speed',
        'vis_min', 'vis_max', 'vis_mean']

    data[floats] = data[floats].astype(float)

    return data


def add_rain_predict(data):
    """
    Adds a rain prediction column to the desired row (day).

    Key arguments:
    data -- The current dataframe.
    """

    def apply(row):

        row['rain_predict'] = get_predict_by_column(data, row, 'rain', 0)

        return row

    return data.apply(apply, axis=1)


def add_rain_fall_predict(data):
    """
    Adds a rain fall prediction column to the desired row (day).

    Key arguments:
    data -- The current dataframe.
    """

    def apply(row):

        row['rain_fall_predict'] = get_predict_by_column(data, row, 'rain_fall', 0.0)

        return row

    return data.apply(apply, axis=1)


def add_snow_accum(data):
    """
    Adds a snow accumulation column for the desired row (day).

    Key arguments:
    data -- The current dataframe.
    """

    def apply(row):
        # Find all of the necessary days in history.
        history = data[
            (data[DATE_COL] >= row[DATE_COL] - np.timedelta64(SNOW_DAYS_HISTORY, 'D')) & \
            (data[DATE_COL] < row[DATE_COL])]

        # Make sure we only have unqiue days.
        history = history.drop_duplicates(DATE_COL)

        # Loop through each day in history and add the weighted snow fall
        #  for that historic day to the snow accumulation for the current day.
        snow_accum = 0.0
        for history_row in history.iterrows():
            # What is the day in history?
            day = history_row[1][DATE_COL]
            # How much snow fall for that day?
            snow_fall = history_row[1]['snow_fall']
            # The weight for the day is the 1/number of days ago
            weight = 1.0 / ((row[DATE_COL] - day).days + 1.0)
            # Add the weighted snow fall to the current accumulation.
            snow_accum += snow_fall * weight

        # Add the current days snow fall to the mix and
        #  add the column to the row.
        row['snow_accum'] = round(snow_accum + row['snow_fall'], 1)

        return row

    return data.apply(apply, axis=1)


def add_snow_accum_predict(data):
    """
    Adds a rain fall prediction column to the desired row (day).

    Key arguments:
    data -- The current dataframe.
    """

    def apply(row):

        row['snow_accum_predict'] = get_predict_by_column(data, row, 'snow_accum', 0.0)

        return row

    return data.apply(apply, axis=1)


def add_snow_predict(data):
    """
    Adds a snow prediction column to the desired row (day).

    Key arguments:
    data -- The current dataframe.
    """

    def apply(row):

        row['snow_predict'] = get_predict_by_column(data, row, 'snow', 0)

        return row

    return data.apply(apply, axis=1)


def add_snow_fall_predict(data):
    """
    Adds a snow fall prediction column to the desired row (day).

    Key arguments:
    data -- The current dataframe.
    """

    def apply(row):

        row['snow_fall_predict'] = get_predict_by_column(data, row, 'snow_fall', 0.0)

        return row

    return data.apply(apply, axis=1)


def get_predict_by_column(data, row, column, default):
    """
    Returns the prediction for a desired column.

    Key arguments:
    data    -- The entire data set.
    row     -- The current row.
    column  -- The desired column to get a prediction for.
    default -- The default value.
    """

    # Initialize todays prediction.
    prediction = default

    # Find the next days prediction
    tomorrow = data[
        data[DATE_COL] == (row[DATE_COL] + np.timedelta64(1, 'D'))
    ]

    # "Todays" prediction is just tomorrow's, if it exists.
    if (len(tomorrow) > 0):
        prediction = tomorrow.iloc[0][column]

    return prediction
