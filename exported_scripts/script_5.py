#!/usr/bin/env openroad -python
from openroad import Tech, Design
from typing import List, Tuple

tech = Tech()
tech.readLef("process.lef")

design = Design(tech)
design.readDef("chip.def")

def get_port_bounding_box(port_name: str = "req_val") -> List[Tuple[float, float]]:
    """
    Return the bounding box of the given port as [(xmin, ymin), (xmax, ymax)].
    """
    block = design.getBlock()
    port  = block.findBTerm(port_name)
    bbox  = port.getBBox()
    return [
        (bbox.xMin(), bbox.yMin()),
        (bbox.xMax(), bbox.yMax())
    ]

bounding_box = get_port_bounding_box()
print(bounding_box)
