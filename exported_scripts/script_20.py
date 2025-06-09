#!/usr/bin/env openroad -python
from openroad import Tech, Design

# ----- 1. setup -----
tech = Tech()
tech.readLef("process.lef")

design = Design(tech)
design.readDef("chip.def")

# ----- 2. set instance orientation -----
block = design.getBlock()
inst  = block.findInst("_411_")
if inst is None:
    raise ValueError("Instance '_411_' not found")

tf = inst.getTransform()
tf.setOrient("MX")
inst.setTransform(tf)
