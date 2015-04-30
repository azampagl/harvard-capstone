#!/usr/bin/env python

"""
This file contains reusable visualization objects.
"""

# Libraries.
from matplotlib import pyplot as plt

# Main chart format. Change to render charts in a different way.
default_chart_format = 'display'

# Figure sizes.
figsize = {
    'default': (12,8),
    'slides': (12,6)
}

# Font sizes.
fontsize = {
    'title': {
        'display': 'x-large',
        'slides': 'xx-large',
        'poster': 24
    },
    'label': {
        'display': 'large',
        'slides': 'x-large',
        'poster': 18
    },
    'ticks': {
        'display': 'medium',
        'slides': 'x-large',
        'poster': 14
    },
    'tick_labels': {
        'display': 'medium',
        'slides': 'x-large',
        'poster': 18
    },
    'game_range': {
        'display': 'large',
        'slides': 'large',
        'poster': 14
    }
}

# Line widths.
line_widths = {
    'display': 3,
    'slides':  3,
    'poster':  4
}

# Line colors.
line_colors = {
    'blue':   (0.44999999999999996, 0.7123853211009172, 1.0),
    'orange': (1.0, 0.6640217391304348, 0.44999999999999996),
    'green':  (0.4010294117647058, 0.8911764705882352, 0.5056675479180436),
    'red':    (1.0, 0.4772277227722773, 0.44999999999999996),
    'annotation': (0.7181372549019608, 0.55, 1.0)
}

# Grid arguments.
grid_settings = {
    'display': { 'b': True },
    'slides':  { 'b': True },
    'poster':  { 'b': False }
}

# Add a game start line.
def game_start_line (color=line_colors['annotation'], line_alpha=1, fontsize='medium'):
    plt.vlines(0, *plt.ylim(), color=color, lw=2, alpha=line_alpha)
    plt.annotate('Game Start', (.05,plt.ylim()[1]*0.95), rotation='vertical', ha='right', color=color, fontsize=fontsize)

# Add a shaded/annotated game range area.
def game_range (game_length, annotate_start=True, annotate_end=False, fontsize='medium'):
    plt.axvspan(0, game_length, color='k', alpha=0.1)
    if annotate_start:
        plt.annotate('Game Start', (-.05,plt.ylim()[1]*0.98), rotation='vertical', va='top', ha='right', color='k', fontsize=fontsize)
    if annotate_end:
        plt.annotate('Game End', (game_length-.05,plt.ylim()[1]*0.98), rotation='vertical', va='top', ha='right', color='k', fontsize=fontsize)

# Add a horizontal line at zero.
def zero_horizontal_line (line_color=line_colors['annotation'], line_alpha=1):
    plt.hlines(0, *plt.xlim(), colors=line_color, lw=2, alpha=line_alpha)
