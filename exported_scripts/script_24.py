#!/usr/bin/env openroad -python
from openroad import Tech, Design
from typing import List, Any

# ----- 1. setup -----
tech = Tech()
tech.readLef("process.lef")

design = Design(tech)
design.readDef("chip.def")

def get_technology_vias() -> List[Any]:
    """
    Return all via definitions (including non-default-rule vias) from the technology.
    """
    block = design.getBlock()
    tech_obj = block.getTech()
    return tech_obj.getVias()

vias = get_technology_vias()
print(vias)
