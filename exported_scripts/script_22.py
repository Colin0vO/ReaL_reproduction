#!/usr/bin/env openroad -python
from openroad import Tech, Design
from typing import int

# ----- 1. setup -----
tech = Tech()
tech.readLef("process.lef")

design = Design(tech)
design.readDef("chip.def")

def get_db_units_per_micron() -> int:
    """
    Return the number of database units per micron for the current design.
    """
    block = design.getBlock()
    return block.getDbUnitsPerMicron()

# ----- 2. invoke -----
db_units_per_micron = get_db_units_per_micron()
print(db_units_per_micron)
