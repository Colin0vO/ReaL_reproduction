#!/usr/bin/env openroad -python
from openroad import Tech, Design
from typing import List

# ----- 1. setup -----
tech = Tech()
tech.readLef("process.lef")

design = Design(tech)
design.readDef("chip.def")

def get_net_cc_adjust_factors() -> List[float]:
    """
    Return the capacitance coupling adjust factor for each net in the design.
    """
    block = design.getBlock()
    return [net.getCcAdjustFactor() for net in block.getNets()]

net_adjust_factors = get_net_cc_adjust_factors()
print(net_adjust_factors)
