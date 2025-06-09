#!/usr/bin/env openroad -python
from openroad import Tech, Design
from typing import Any

# ----- 1. setup -----
tech = Tech()
tech.readLef("process.lef")

design = Design(tech)
design.readDef("chip.def")

def check_if_any_wire_altered() -> bool:
    """
    Return True if any net in the design block has an altered wire.
    """
    return any(
        net.isWireAltered()
        for net in design.getBlock().getNets()
    )

is_wire_altered = check_if_any_wire_altered()
print(is_wire_altered)
