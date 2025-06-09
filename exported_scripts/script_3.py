#!/usr/bin/env openroad -python
from openroad import Tech, Design, get_timing
from typing import List, Any

# ----- 1. setup -----
tech = Tech()
tech.readLef("process.lef")

design = Design(tech)
design.readDef("chip.def")

# ----- 2. gather pins with arrival > 0.5 -----
block  = design.getBlock()
timing = get_timing()

def get_slow_pins(threshold: float = 0.5) -> List[Any]:
    """
    Return all instance pins whose rise arrival exceeds the given threshold.
    """
    return [
        pin
        for inst in block.getInsts()
        for pin in inst.getITerms()
        if not design.isInSupply(pin)
        and timing.getPinArrival(pin, timing.Rise) > threshold
    ]

slow_pins = get_slow_pins()
print(slow_pins)
