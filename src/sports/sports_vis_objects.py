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
        'slides': 'xx-large'
    },
    'label': {
        'display': 'large',
        'slides': 'x-large'
    },
    'ticks': {
        'display': 'medium',
        'slides': 'x-large'
    },
    'game_range': {
        'display': 'large',
        'slides': 'large'
    }
}

# Add a game start line.
def game_start_line (color='indigo',  line_alpha=.5, fontsize='medium'):
    plt.axvline(0, *plt.ylim(), color=color, lw=2, alpha=line_alpha)
    plt.annotate('Game Start', (.05,plt.ylim()[1]*0.95), rotation='vertical', ha='right', color=color, fontsize=fontsize)

# Add a shaded/annotated game range area.
def game_range (game_length, annotate_start=True, annotate_end=False, fontsize='medium'):
    plt.axvspan(0, game_length, color='k', alpha=0.1)
    if annotate_start:
        plt.annotate('Game Start', (-.05,plt.ylim()[1]*0.98), rotation='vertical', va='top', ha='right', color='k', fontsize=fontsize)
    if annotate_end:
        plt.annotate('Game End', (game_length-.05,plt.ylim()[1]*0.98), rotation='vertical', va='top', ha='right', color='k', fontsize=fontsize)

# Add a horizontal line at zero.
def zero_horizontal_line (line_color='indigo', line_alpha=.5):
    plt.hlines(0, *plt.xlim(), colors=line_color, lw=2, alpha=line_alpha)