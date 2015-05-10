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
    'display': (12,8),
    'slides':  (12,6),
    'poster':  (9.75,6.5),
    'poster_small': (3,2),
    'report_inline': (3.3, 3)
}

# Font sizes.
fontsize = {
    'title': {
        'display': 'x-large',
        'slides': 'xx-large',
        'poster': 24,
        'poster_small': 14,
        'report_inline': 8
    },
    'label': {
        'display': 'large',
        'slides': 'x-large',
        'poster': 18,
        'poster_small': 12,
        'report_inline': 7
    },
    'legend': {
        'display': 'large',
        'slides': 'x-large',
        'poster': 18,
        'poster_small': 12,
        'report_inline': 7
    },
    'ticks': {
        'display': 'medium',
        'slides': 'x-large',
        'poster': 14,
        'poster_small': 10,
        'report_inline': 7
    },
    'tick_labels': {
        'display': 'medium',
        'slides': 'x-large',
        'poster': 18,
        'poster_small': 12,
        'report_inline': 9
    },
    'game_range': {
        'display': 'large',
        'slides': 'large',
        'poster': 14,
        'poster_small': 10,
        'report_inline': 8
    }
}

# Line widths.
line_widths = {
    'display':       3,
    'slides':        3,
    'poster':        4,
    'poster_small':  3,
    'report_inline': 2
}

# Grid arguments.
grid_settings = {
    'display': { 'b': True },
    'slides':  { 'b': True },
    'poster':  { 'b': False },
    'poster_small':  { 'b': False },
    'report_inline': { 'b': True, 'lw':.25 }
}

# Annotation color.
line_annotation_default = (0.7181372549019608, 0.55, 1.0)

# Add a game start line.
def game_start_line (color=line_annotation_default, line_alpha=1, show_text=True, fontsize='medium', axis_rev=True):
    plt.vlines(0, *plt.ylim(), color=color, lw=2, alpha=line_alpha)
    if show_text:
        plt.annotate('Game Start', (.05 * (1 if axis_rev else -1),plt.ylim()[1]*0.95), rotation='vertical', ha='right', color=color, fontsize=fontsize)

# Add a shaded/annotated game range area.
def game_range (game_length, annotate_start=True, annotate_end=False, fontsize='medium'):
    plt.axvspan(0, game_length, color='k', alpha=0.1)
    if annotate_start:
        plt.annotate('Game Start', (-.05,plt.ylim()[1]*0.98), rotation='vertical', va='top', ha='right', color='k', fontsize=fontsize)
    if annotate_end:
        plt.annotate('Game End', (game_length-.05,plt.ylim()[1]*0.98), rotation='vertical', va='top', ha='right', color='k', fontsize=fontsize)

# Add a horizontal line at zero.
def zero_horizontal_line (line_color=line_annotation_default, line_alpha=1):
    plt.hlines(0, *plt.xlim(), colors=line_color, lw=2, alpha=line_alpha)
