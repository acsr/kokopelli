"""
@namespace machines
@brief Module containing output machines

@details  Each input module must define NAME, INPUT, PANEL, and DEFAULTS (a list of tuples, each containing a default name and a dictionary which defines defaults for each potential panel).
"""

import mimaki650, modela, epilog, universal, null, shopbot, gcode, shopbot5

MACHINES = [null, mimaki650, modela, epilog, universal, shopbot, gcode, shopbot5]
