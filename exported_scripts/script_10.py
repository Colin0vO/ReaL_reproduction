#!/usr/bin/env openroad -python
from openroad import Tech, Design
from typing import Any, List

# ----- 1. setup -----
tech = Tech()
tech.readLef("process.lef")

design = Design(tech)
design.readDef("chip.def")

def get_cc_segments() -> List[Any]:
    """
    Return all capacitor‑coupled segments in the current design block.
    """
    block = design.getBlock()
    return block.getCCSegs()

cc_segments = get_cc_segments()
print(cc_segments)
