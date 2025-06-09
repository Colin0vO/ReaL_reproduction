#!/usr/bin/env openroad -python
from openroad import Tech, Design
from typing import Any, List

# ----- 1. setup -----
tech = Tech()
tech.readLef("process.lef")

design = Design(tech)
design.readDef("chip.def")

def get_resistor_segments() -> List[Any]:
    """
    Return all resistor segments in the current design block.
    """
    return design.getBlock().getRSegs()

r_segments = get_resistor_segments()
print(r_segments)
