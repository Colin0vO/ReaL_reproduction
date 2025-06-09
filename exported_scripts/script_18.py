#!/usr/bin/env openroad -python
from openroad import Tech, Design
from typing import float

# ----- 1. setup -----
tech = Tech()
tech.readLef("process.lef")

design = Design(tech)
design.readDef("chip.def")

def get_clearance_measure() -> float:
    """
    Return the clearance measure defined in the technology.
    """
    return design.getBlock().getTech().getClearanceMeasure()

# ----- 2. invoke -----
clearance_measure = get_clearance_measure()
print(clearance_measure)
