#!/usr/bin/env openroad -python
from openroad import Tech, Design

# ----- 1. setup -----
tech = Tech()
tech.readLef("process.lef")

design = Design(tech)
design.readDef("chip.def")

# ----- 2. reposition instance -----
block = design.getBlock()
inst  = block.findInst("input2")
if inst is None:
    raise ValueError("Instance 'input2' not found")
inst.setLocation(22500, 33459)
