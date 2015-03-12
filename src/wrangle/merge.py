"""
Takes the gatecount csv and weather csv and merges them.

The style guide follows the strict python PEP 8 guidelines.
@see http://www.python.org/dev/peps/pep-0008/

@author Aaron Zampaglione <azampaglione@g.harvard.edu>

@requires Python >=2.7
@copyright 2015
"""
import getopt
import os
import sys

import pandas as pd

from datetime import datetime, timedelta

def main(args):
    """
    Main execution.

    Key arguments:
    args -- A dictionary of the arguments passed via command line.
    """

    # Load in the two data sets.
    stations = pd.read_csv(args['s'])
    gatecounts = pd.read_csv(args['g'])
    weather = pd.read_csv(args['w'])

    # Merge the data sets.
    data = pd.merge(stations, gatecounts, how='right', left_on='stationid', right_on='locationid')
    data = pd.merge(data, weather, how='left', left_on='service_day', right_on='date')

    # Drop the two columns we merged on.
    data.drop('locationid', axis=1, inplace=True)
    data.drop('date', axis=1, inplace=True)

    # Rename stationid to columnid for legacy support of everyones code.
    data.rename(columns={'stationid': 'locationid'}, inplace=True)

    # Save to disk.
    data.to_csv(args['o'], index=False)


def usage():
    """Prints the usage of the program."""

    print("\n" +
    "The following are arguments required:\n" +
    "\t-g: the input gatecount csv file.\n" +
    "\t-w: the input weather csv file.\n" +
    "\t-s: the stations csv file.\n" +
    "\t-o: the output csv file.\n" +
    "\n" +
    "Example Usage:\n" +
    "\tpython merge.py " + \
    "-g \"./gatecounts.csv\" " + \
    "-w \"./weather.csv\" " + \
    "-s \"./stations.csv\" " + \
    "-o \"./mbta.csv\"\n" +
    "\n")


"""Main execution."""
if __name__ == "__main__":

    # Determine command line arguments.
    try:
        rawargs, _ = getopt.getopt(sys.argv[1:], 'g:w:s:o:')
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    args = {}

    # Process each command line argument.
    for o, a in rawargs:
        args[o[1]] = a

    # The following arguments are required in all cases.
    for arg in ['g', 'w', 's', 'o']:
        if not arg in args:
            usage()
            sys.exit(2)

    main(args)
