#!/usr/bin/env python3
"""
Enable the reapy distant API in REAPER.

Run this script from within REAPER:
  1. Open REAPER
  2. Go to Actions > Run ReaScript
  3. Select this file

After running, restart REAPER for the changes to take effect.
"""

import reapy

reapy.config.enable_dist_api()
print("reapy distant API enabled. Please restart REAPER.")
