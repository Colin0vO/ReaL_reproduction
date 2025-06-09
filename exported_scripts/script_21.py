#!/usr/bin/env openroad -python
from openroad import Tech, Design

# ----- 1. setup -----
tech = Tech()
tech.readLef("process.lef")

design = Design(tech)
design.readDef("chip.def")

# ----- 2. reset tapcell -----
def reset_tapcell() -> None:
    """
    Reset the tapcell in the design.
    """
    tapcell = design.getTapcell()
    tapcell.reset()

reset_tapcell()
