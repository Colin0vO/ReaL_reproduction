#!/usr/bin/env openroad -python
from openroad import Tech, Design
from typing import Any, List

# ----- 1. setup -----
tech = Tech()
tech.readLef("process.lef")

design = Design(tech)
design.readDef("chip.def")

# ----- 2. retrieve forbidden spacing rules for via8 -----
block = design.getBlock()
tech_obj = block.getTech()
layer = tech_obj.findLayer("via8")
forbidden_rules: List[Any] = layer.getTechLayerForbiddenSpacingRules()

print(forbidden_rules)
