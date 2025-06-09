#!/usr/bin/env openroad -python
from openroad import Tech, Design

# ----- 1. setup -----
tech = Tech()
tech.readLef("process.lef")

design = Design(tech)
design.readDef("chip.def")

# ----- 2. invert NAND2_X1 instances -----
block = design.getBlock()
for inst in block.getInsts():
    if inst.getMaster().getName() == "NAND2_X1":
        tf = inst.getTransform()
        tf.invert()
        inst.setTransform(tf)
