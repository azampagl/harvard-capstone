"""
Adds additional entry features to a data set.

The style guide follows the strict python PEP 8 guidelines.
@see http://www.python.org/dev/peps/pep-0008/

@author Aaron Zampaglione <azampaglione@g.harvard.edu>

@requires Python >=2.7
@copyright 2015
"""
import numpy as np
import pandas as pd


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
    data['service_day'] = pd.to_datetime(data['service_day'])
    data['service_datetime'] = pd.to_datetime(data['service_datetime'])

    # Set indices.
    #data = data.set_index('service_day', append=True)
    #data = data.set_index('service_datetime', append=True)

    return data


def add_previous_week(data, weeks_ago = 1, day_col = 'service_datetime'):
    """
    Adds a column that has the same entries one week ago.

    Key arguments:
    data  -- The current dataframe.
    weeks -- The number of weeks to look back.
    """

    def apply(row):
        # Find the previous day x weeks ago.
        previous_day = row[day_col] - np.timedelta64(weeks_ago, 'W')

        # Find the entries for this stations exactly x weeks ago.
        entries = data.loc[
            (data[day_col] == previous_day) &
            (data['locationid'] == row['locationid'])
        ]['entries'].values

        # Set the entries from X weeks ago.
        column = 'entries_weeks_ago_' + str(weeks_ago)
        row[column] = np.nan
        if (len(entries) == 1):
            row[column] = entries[0]

        return row

    return data.apply(apply, axis=1)
