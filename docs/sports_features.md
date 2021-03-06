# Sports Features

This document describes the features that describe Bruins, Celtics, and Red Sox gamedays. Extremely granular features (e.g., binary indicators for particular game days/times) are not feasible for prediction, so we need to find reasonable ways to group games. Bruins and Red Sox games are fairly diverse in their scheduling and allow us to derive several groupings; Celtics games are more "monolithic" and lend themselves to a small set of large groups.

Fields in `game_days.csv` (generated by `/src/sports/sports_features.ipynb`) describe games based on days of week and time of day. These include intuitive groupings across days (e.g., Monday-Thursday evenings, Friday/Saturday evenings, etc.). The most simple features indicate that a specific team played a home game on that date:

- bruins_game
- celtics_game
- sox_game

Those may be useful on their own for prediction. The following fields likely constitute more useful groupings.

### Bruins Fields

- bruins_mon_fri_early
- bruins_mon_thu_late
- bruins_fri_sat_late
- bruins_sat_early
- bruins_sun

"buins_mon_fri_early" has only 6 records and may need to be combined with another group for prediction.

### Celtics Fields

- celtics_mon_thu
- celtics_fri_sat
- celtics_sun

### Red Sox Fields

- sox_fri_late
- sox_sat_early
- sox_sat_late
- sox_sun_early
- sox_sun_late
- sox_mon_thu_late
- sox_mon_fri_early

"sox_sun_late" shows relatively few records (8) and may need to be combined with another group.
