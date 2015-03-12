"""
Adds additional time features to a gatecount/weather data set.

The style guide follows the strict python PEP 8 guidelines.
@see http://www.python.org/dev/peps/pep-0008/

@author Aaron Zampaglione <azampaglione@g.harvard.edu>

@requires Python >=2.7
@copyright 2015
"""
import pandas as pd


#
# Consts
#


# Minutes in an hour.
MINUTES_PER_HOUR = 60


#
# Methods.
#


def init(data):
    """
    Initializes the current columns to the proper data type(s).

    Key arguments:
    date  -- The current dataframe.
    """

    # Convert the date fields.
    data['service_datetime'] = pd.to_datetime(data['service_datetime'])

    # Add index.
    #data = data.set_index('service_datetime', append=True)

    return data


def add_day_of_week(data):
    """
    Adds a day of the week feature.

    Key arguments:
    data -- The data to augment to.
    """

    data['day_of_week'] = pd.DatetimeIndex(data['service_datetime']).weekday

    return data


def add_day_of_week_binary(data):
    """
    Adds a day of the week feature as a binary column.

    Key arguments:
    data -- The data to augment to.
    """

    def apply(row):
        # Find the current weekday.
        dow = row['service_datetime'].weekday()

        # 7 days in a week, Monday=0.
        for i in xrange(7):
            # Determine the column name.
            column = 'day_of_week_' + str(i)
            # Initialize to 0.
            row[column] = 0
            # If it is the current day of the week, set it to one
            if (i == dow):
                row[column] = 1

        return row

    return data.apply(apply, axis=1)


def add_hour_binary(data):
    """
    Adds hour as a binary column.

    Key arguments:
    data -- The data to augment to.
    """

    def apply(row):
        # Find the current weekday.
        hour = row['service_datetime'].hour

        # Loop through each month
        for i in xrange(0, 24):
            # Determine the column name.
            column = 'hour_' + str(i)
            # Initialize to 0.
            row[column] = 0
            # If it is the current day of the week, set it to one
            if (i == hour):
                row[column] = 1

        return row

    return data.apply(apply, axis=1)


def add_month_binary(data):
    """
    Adds month as a binary column.

    Key arguments:
    data -- The data to augment to.
    """

    def apply(row):
        # Find the current weekday.
        month = row['service_datetime'].month

        # Loop through each month
        for i in xrange(1, 13):
            # Determine the column name.
            column = 'month_' + str(i)
            # Initialize to 0.
            row[column] = 0
            # If it is the current day of the week, set it to one
            if (i == month):
                row[column] = 1

        return row

    return data.apply(apply, axis=1)


def add_weekend(data):
    """
    Adds a binary column representing weekend/weekday.

    Key arguments:
    data -- The data to augment to.
    """

    def apply(row):
        # Find the current weekday.
        dow = row['service_datetime'].weekday()

        # Determine the column name.
        column = 'weekend'
        # Initialize to 0.
        row[column] = 0
        # If it is the current day of the week, set it to one
        if (dow == 5 or dow == 6):
            row[column] = 1

        return row

    return data.apply(apply, axis=1)


def add_service_minutes_fraction(data):
    """
    Adds a column with minutes as a fraction of an hour.

    Key arguments:
    data -- The data to augment to.
    """

    data['service_minutes_fraction'] = pd.DatetimeIndex(
        data['service_datetime']).minute \
        / float(MINUTES_PER_HOUR)

    return data
