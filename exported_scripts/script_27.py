#!/usr/bin/env openroad -python
from openroad import Tech, Design
from pathlib import Path
import argparse

def setup_design(chip: str, lef: str, dfn: str) -> Design:
    tech = Tech()
    tech.readLef(lef)
    
    design = Design(tech)
    design.readDef(dfn)
    return design

def get_clearance_measure(design: Design):
    """
    Return the clearance measure defined in the technology.
    """
    tech_obj = design.getBlock().getTech()
    return tech_obj.getClearanceMeasure()

def main():
    parser = argparse.ArgumentParser(
        description="Retrieve the technology clearance measure"
    )
    parser.add_argument("--chip", default="chip", help="Design name (no extension)")
    parser.add_argument("--lef",  default="process.lef", help="LEF file path")
    parser.add_argument("--def",  dest="dfn", default="chip.def", help="DEF file path")
    args = parser.parse_args()

    for path in (args.lef, args.dfn):
        if not Path(path).exists():
            parser.error(f"File not found: {path}")

    design = setup_design(args.chip, args.lef, args.dfn)
    cm = get_clearance_measure(design)
    print(f"Technology clearance measure: {cm}")

if __name__ == "__main__":
    main()
