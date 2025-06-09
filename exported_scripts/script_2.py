#!/usr/bin/env openroad -python
from openroad import Tech, Design
from typing import List

# ----- 1. setup -----
tech = Tech()
tech.readLef("process.lef")

design = Design(tech)
design.readDef("chip.def")

def get_module_names() -> List[str]:
    """
    Return a list of all module names in the current design.
    """
    block = design.getBlock()
    return [mod.getName() for mod in block.getModules()]

module_names_list = get_module_names()
print(module_names_list)
