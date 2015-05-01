#!/usr/bin/env python

"""
This file contains reusable sports settings information that we can share between files.
"""

# Teams.
teams = ['bruins','celtics','sox']

# Team names.
team_names = {
    'bruins':  'Bruins',
    'celtics': 'Celtics',
    'sox':     'Red Sox'
}

# Game lengths in hours for coloring.
team_game_lengths = {
    'bruins':  2.3333,
    'celtics': 2.25,
    'sox':     3+8./60
}

# Line colors.
line_colors = {
    'blue':   (0.44999999999999996, 0.7123853211009172, 1.0),
    'orange': (1.0, 0.6640217391304348, 0.44999999999999996),
    'green':  (0.4010294117647058, 0.8911764705882352, 0.5056675479180436),
    'red':    (1.0, 0.4772277227722773, 0.44999999999999996)
}

# Team colors.
team_colors = {
    'bruins':  '#FDB930',
    'celtics': '#008348',
    'sox':     '#BD3039'
}
team_colors_pastel = {
    'bruins':  line_colors['orange'],
    'celtics': line_colors['green'],
    'sox':     line_colors['red']
}

# Team stations.
team_stations = {
    'bruins':  'North Station',
    'celtics': 'North Station',
    'sox':     'Kenmore & Hynes'
}

# Lines.
lines = ['blue','green','orange','red']
line_names = [l.title() for l in lines]

# Columns.
line_lift_cols = ['lift_entries_'+l for l in lines]

# Day of week mapping.
days_of_week = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']