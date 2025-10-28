#!/usr/bin/env python3
"""
Automatically generates materials/index.json by scanning the materials folder for JSON files.
Run this script whenever you add new quiz files to the materials folder.
"""

import json
import os
from pathlib import Path

def update_materials_index():
    materials_dir = Path(__file__).parent / "materials"

    if not materials_dir.exists():
        print(f"Error: {materials_dir} does not exist")
        return

    # Find all JSON files in materials folder (excluding index.json itself)
    json_files = sorted([
        f.name for f in materials_dir.glob("*.json")
        if f.name != "index.json"
    ])

    # Write to index.json
    index_file = materials_dir / "index.json"
    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(json_files, f, indent=2, ensure_ascii=False)

    print(f"✓ Updated {index_file}")
    print(f"  Found {len(json_files)} quiz files:")
    for filename in json_files:
        print(f"    - {filename}")

if __name__ == "__main__":
    update_materials_index()
