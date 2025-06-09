#!/usr/bin/env openroad -python
from openroad import Tech, Design
from typing import List, Any

# ----- 1. setup -----
tech = Tech()
tech.readLef("process.lef")

design = Design(tech)
design.readDef("chip.def")

def get_wild_connected_nets() -> List[Any]:
    """
    Return all nets in the design block that are wild-connected.
    """
    return [
        net
        for net in design.getBlock().getNets()
        if net.isWildConnected()
    ]

wild_connected_nets = get_wild_connected_nets()
print(wild_connected_nets)
