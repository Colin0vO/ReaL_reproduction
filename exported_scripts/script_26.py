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

def get_db_units_per_micron(design: Design):
    """
    Return the number of database units (DBU) per micron.
    """
    block = design.getBlock()
    return block.getDbUnitsPerMicron()

def main():
    parser = argparse.ArgumentParser(
        description="Query DB units per micron for this technology"
    )
    parser.add_argument("--chip", default="chip", help="Design name (no extension)")
    parser.add_argument("--lef",  default="process.lef", help="LEF file path")
    parser.add_argument("--def",  dest="dfn", default="chip.def", help="DEF file path")
    args = parser.parse_args()

    for path in (args.lef, args.dfn):
        if not Path(path).exists():
            parser.error(f"File not found: {path}")

    design = setup_design(args.chip, args.lef, args.dfn)
    dbu    = get_db_units_per_micron(design)
    print(f"DB units per micron: {dbu}")

if __name__ == "__main__":
    main()
