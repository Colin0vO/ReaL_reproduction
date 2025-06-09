#!/usr/bin/env openroad -python
from openroad import Tech, Design
from typing import int

# ----- 1. setup -----
tech = Tech()
tech.readLef("process.lef")

design = Design(tech)
design.readDef("chip.def")

def get_via_count() -> int:
    """
    Return the total number of vias defined in the technology.
    """
    block = design.getBlock()
    return block.getTech().getViaCount()

via_count = get_via_count()
print(via_count)
