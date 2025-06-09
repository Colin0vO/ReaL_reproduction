#!/usr/bin/env openroad -python
from openroad import Tech, Design
from typing import List
from pathlib import Path
import argparse

def setup_design(chip: str, lef: str, dfn: str) -> Design:
    tech = Tech()
    tech.readLef(lef)
    
    design = Design(tech)
    design.readDef(dfn)
    return design

def get_instance_names(design: Design) -> List[str]:
    """
    Return a list of all instance names in the design block.
    """
    block = design.getBlock()
    return [inst.getName() for inst in block.getInsts()]

def main():
    parser = argparse.ArgumentParser(
        description="List all instance names in the design"
    )
    parser.add_argument("--chip",  default="chip", help="Design name (no extension)")
    parser.add_argument("--lef",   default="process.lef", help="LEF file path")
    parser.add_argument("--def",   dest="dfn", default="chip.def", help="DEF file path")
    args = parser.parse_args()

    # Verify files exist
    for path in (args.lef, args.dfn):
        if not Path(path).exists():
            parser.error(f"File not found: {path}")

    design = setup_design(args.chip, args.lef, args.dfn)
    names  = get_instance_names(design)
    print(f"Found {len(names)} instances:")
    for name in names:
        print("  -", name)

if __name__ == "__main__":
    main()
