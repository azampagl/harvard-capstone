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
    gatecounts = pd.read_csv(args['g'])
    weather = pd.read_csv(args['w'])

    # Rename the date column to match the gatecount day column.
    weather.rename(columns={'date': 'service_day'}, inplace=True)

    # Merge the two columns.
    data = pd.merge(gatecounts, weather, how='left')
    
    # Save to disk.
    data.to_csv(args['o'], index=False)


def usage():
    """Prints the usage of the program."""

    print("\n" +
    "The following are arguments required:\n" +
    "\t-g: the input gatecount csv file.\n" +
    "\t-w: the input weather csv file.\n" +
    "\t-o: the output csv file.\n" +
    "\n" +
    "Example Usage:\n" +
    "\tpython gatecount-weather-merge.py " + \
    "-g \"./gatecounts.csv\" " + \
    "-w \"./weather.csv\" " + \
    "-o \"./gatecounts-weather.csv\"\n" +
    "\n")


"""Main execution."""
if __name__ == "__main__":

    # Determine command line arguments.
    try:
        rawargs, _ = getopt.getopt(sys.argv[1:], 'g:w:o:')
    except getopt.GetoptError:
        usage()
        sys.exit(2)

    args = {}

    # Process each command line argument.
    for o, a in rawargs:
        args[o[1]] = a

    # The following arguments are required in all cases.
    for arg in ['g', 'w', 'o']:
        if not arg in args:
            usage()
            sys.exit(2)

    main(args)
