"""
Adds additional station features to a data set.

The style guide follows the strict python PEP 8 guidelines.
@see http://www.python.org/dev/peps/pep-0008/

@author Aaron Zampaglione <azampaglione@g.harvard.edu>

@requires Python >=2.7
@copyright 2015
"""
import numpy as np
import pandas as pd


#
# Consts.
#


CITY_CENTER = np.array([42.3601637, -71.0577871])


#
# Methods.
#


def init(data):
    """
    Initializes the current columns to the proper data type(s).

    Key arguments:
    data -- The current dataframe.
    """

    # Convert the floating fields.
    data[['lat', 'lon']] = data[['lat', 'lon']].astype(float)

    return data


def add_distance_to_center(data):
    """
    Adds a column which is the distance to the city center.

    Key arguments:
    data  -- The current dataframe.
    """

    # Radius of the earth in KM.
    r = 6371

    # Convert the city center to radians.
    center = CITY_CENTER * np.pi / 180.0
    cos_lat2 = np.cos(center[0])

    # Keep a cache so we only have to calculate the distance once for each location.
    cache = {}

    def apply(row):
        dist = np.nan

        if (row['locationid'] in cache):
            dist = cache[row.locationid]
        else:
            pos = np.array([row['lat'], row['lon']])
            pos = pos * np.pi / 180.0

            cos_lat1 = np.cos(pos[0])
            cos_lat_d = np.cos(pos[0] - center[0])
            cos_lon_d = np.cos(pos[1] - center[1])

            dist = r * np.arccos(cos_lat_d - cos_lat1 * cos_lat2 * (1 - cos_lon_d))

            cache[row['locationid']] = dist

        row['dist_to_center'] = dist

        return row

    return data.apply(apply, axis=1)
