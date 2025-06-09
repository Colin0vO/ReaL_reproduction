#!/usr/bin/env openroad -python
from openroad import Tech, Design
from typing import Optional

# ----- 1. setup -----
tech = Tech()
tech.readLef("process.lef")

design = Design(tech)
design.readDef("chip.def")

def calibrate_net_cc(net_name: str = "req_msg[11]", factor: float = 2.0) -> None:
    """
    Set the capacitance coupling calibration factor for the specified net.
    """
    block = design.getBlock()
    net = block.findNet(net_name)
    if net is None:
        raise ValueError(f"Net '{net_name}' not found in block")
    net.setCcCalibFactor(factor)

# ----- 2. calibrate the net -----
calibrate_net_cc()
