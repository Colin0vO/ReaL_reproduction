#!/usr/bin/env openroad -python
from openroad import Tech, Design
from typing import Any

# ----- 1. setup -----
tech = Tech()
tech.readLef("process.lef")

design = Design(tech)
design.readDef("chip.def")

def get_iop_vertical_thickness(corner_avoidance: int = 50) -> Any:
    """
    Configure the IO pin placer’s corner avoidance and return the vertical thickness multiplier.
    """
    iop    = design.getIOPlacer()
    params = iop.getParameters()
    params.setCornerAvoidance(corner_avoidance)
    return params.getVerticalThicknessMultiplier()

vertical_thickness = get_iop_vertical_thickness()
print(vertical_thickness)
