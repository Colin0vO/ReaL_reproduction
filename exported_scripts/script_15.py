#!/usr/bin/env openroad -python
from openroad import Tech, Design
from typing import Any, List

# ----- 1. setup -----
tech = Tech()
tech.readLef("process.lef")

design = Design(tech)
design.readDef("chip.def")

# ----- 2. retrieve min‑cut rules for metal1 -----
block = design.getBlock()
layer = block.getTech().findLayer("metal1")
min_cut_rules: List[Any] = layer.getTechLayerMinCutRules()

print(min_cut_rules)
