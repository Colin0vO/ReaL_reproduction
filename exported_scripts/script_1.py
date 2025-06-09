#!/usr/bin/env openroad -python
from openroad import Tech, Design
from typing import Dict, Any

# ----- 1. setup -----
tech = Tech()
tech.readLef("process.lef")

design = Design(tech)
design.readDef("chip.def")

def get_instances_and_regions(skip_prefix: str = "FILLER") -> Dict[str, Any]:
    """
    Return a mapping from each non‑filler instance name to its region,
    suppressing spurious filler‑cell warnings.
    """
    block = design.getBlock()
    inst_regions: Dict[str, Any] = {}
    for inst in block.getInsts():
        name = inst.getName()
        if name.startswith(skip_prefix):
            continue
        inst_regions[name] = inst.getRegion()
    return inst_regions

instances_and_regions = get_instances_and_regions()
print(instances_and_regions)
