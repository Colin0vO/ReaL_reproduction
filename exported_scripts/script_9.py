#!/usr/bin/env openroad -python
from openroad import Tech, Design
from typing import Dict

# ----- 1. setup -----
tech = Tech()
tech.readLef("process.lef")

design = Design(tech)
design.readDef("chip.def")

def get_layer_areas() -> Dict[str, float]:
    """
    Return a mapping from each technology layer name to its area parameter.
    """
    tech_obj = design.getBlock().getTech()
    return {layer.getName(): layer.getArea() for layer in tech_obj.getLayers()}

layer_areas = get_layer_areas()
print(layer_areas)
