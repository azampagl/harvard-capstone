"""
Takes the gatecount csv files from a folder and wrangles
them into one csv file.

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

from datetime import datetime, timedelta

#
# Constants
#

# String used to convert a string into a datetime object.
DATETIME_STR = "%Y/%m/%d"

# Minutes in an hour.
MINUTES_PER_HOUR = 60


#
# Methods
#

def process(data, start, end):
    """
    Processes the dataframe and returns a wrangled
    data frame.

    This will fix the service times and make sure the the values are within
    the date range provided.

    If the features boolean is provided, additional features will be added.

    Key arguments:
    data     -- The pandas dataframe (csv file).
    start    -- The start datetime.
    end      -- The end datetime.
    """

    # Convert the servicedate field to a datetime object.
    #  This is the actual start day of the service.
    data['service_day'] = pd.to_datetime(data['servicedate'])

    # Make sure the date is withing range.
    data = data[(data['service_day'] >= start) & (data['service_day'] <= end)]

    # Find the actual service datetime.
    data['service_datetime'] = data['service_day'] + np.array( \
        np.floor(data['servicetime'] / 100) * MINUTES_PER_HOUR \
        + np.mod(data['servicetime'], 100),
        dtype='timedelta64[m]')

    data.drop('servicedate', axis=1, inplace=True)
    data.drop('servicetime', axis=1, inplace=True)

    return data


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
    data = pd.DataFrame()

    for root, dirs, files in os.walk(args['i']):
        for file in files:
            with open(os.path.join(root, file), 'r') as file_handle:
                data = data.append(
                    process(
                        pd.read_csv(file_handle),
                        args['s'],
                        args['e']))

    # Save to disk.
    data.to_csv(args['o'], index=False)


def usage():
    """Prints the usage of the program."""

    print("\n" +
    "The following are arguments required:\n" +
    "\t-i: the input directory containing the csv files.\n" +
    "\t-s: the (inclusive) start date (e.g. \"2015/01/01\").\n" +
    "\t-e: the (inclusive) end date (e.g. \"2015/01/31\").\n" +
    "\t-o: the output csv file.\n" +
    "\n" +
    "Example Usage:\n" +
    "\tpython gatecount-wrangle.py " + \
    "-i \"./GateCounts\" " + \
    "-s \"2015/01/01\" " + \
    "-e \"2015/01/31\" " + \
    "-o \"./gatecounts.csv\"\n" +
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
