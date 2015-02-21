Boston Daily Normals
====================

Daily normal weather statistics come from [NOAA data](http://www.erh.noaa.gov/box/climate/bosnml.shtml). CSV-formatted data is stored in the repository, as it is compact and static—it does not change over time for our purposes. Values are unchanged from the source, except for converting "-0.0" `SnwG` values into unsigned values for clarity.

For reference, here are the field labels and definitions:

    MoDy      Month and Day
    MaxT      Maximum Temperature
    AveT      Average Temperature
    MinT      Minimum Temperature
    HDD       Daily Heating Degree Days
    MHDD      Cumulative Monthly Heating Degree Days
    CDD       Daily Cooling Degree Days
    MCDD      Cumulative Monthly Cooling Degree Days
    PcpD      Daily Precipitation
    PcpM      Cumulative Monthly Precipitation
    SnwD      Daily Snowfall
    SnwM      Cumulative Montly Snowfall
    SnwG      Snow On The Ground
    PcpYr     Cumulative Precipitation For The Year

Field names are unchanged from the source above, save for removing a space from the "Mo Dy" field.