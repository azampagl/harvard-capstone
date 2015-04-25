#!/usr/bin/env python

"""
This file contains reusable sports settings information that we can share between files.
"""

# Teams.
teams = ['bruins','celtics','sox']
team_names = ['Bruins','Celtics','Red Sox']

# Game lengths in hours for coloring.
game_lengths = {
    'bruins':  2.3333,
    'celtics': 2.25,
    'sox':     3+8./60
}

# Team colors.
team_colors = {
    'bruins':  '#FDB930',
    'celtics': '#008348',
    'sox':     '#BD3039'
}

# Lines.
lines = ['blue','green','orange','red']
line_names = [l.title() for l in lines]

# Columns.
line_lift_cols = ['lift_entries_'+l for l in lines]

# Day of week mapping.
days_of_week = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']