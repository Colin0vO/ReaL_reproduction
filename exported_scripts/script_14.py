#!/usr/bin/env openroad -python
from openroad import Tech, Design
from typing import Dict, Any

# ----- 1. setup -----
tech = Tech()
tech.readLef("process.lef")

design = Design(tech)
design.readDef("chip.def")

# ----- 2. collect port → pin mappings -----
block = design.getBlock()
ports = block.getBTerms()

port_pin_map: Dict[str, Any] = {
    port.getName(): port.getBPins()
    for port in ports
}

print(port_pin_map)
