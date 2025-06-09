#!/usr/bin/env openroad -python
from openroad import Tech, Design

# ----- 1. setup -----
tech = Tech()
tech.readLef("process.lef")

design = Design(tech)
design.readDef("chip.def")

def set_net_cc_adjust_order(net_name: str = "req_msg[13]", order: int = 1) -> None:
    """
    Locate the specified net and set its capacitance coupling adjust order.
    """
    block = design.getBlock()
    net = block.findNet(net_name)
    if net is None:
        raise ValueError(f"Net '{net_name}' not found")
    net.setCcAdjustOrder(order)

# ----- 2. apply adjustment -----
set_net_cc_adjust_order()
