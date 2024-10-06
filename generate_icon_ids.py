import json
import argparse
# import os

# Usage: python3 generate_icon_ids.py ./icons.json
parser = argparse.ArgumentParser(description='Generate icon ids')
parser.add_argument('icons', type=str, help='Path to icons.json')

args = parser.parse_args()

with open(args.icons, 'r') as f:
    icons = json.load(f)
ids = {}
for item in icons:
    if item.get('Properties') is not None:
        if item["Properties"].get("mIconData") is not None:
            for icon in item["Properties"]["mIconData"]:
                if icon.get('Id') is not None:
                    print("Getting Icon ID: ", icon["Id"])
                    if icon["IconName"].get("SourceString") is not None:
                        ids[icon["Id"]] = icon["IconName"]["SourceString"]
                    else:
                        ids[icon["Id"]] = icon["IconName"]["CultureInvariantString"]

with open('icon_ids.json', 'w') as f:
    json.dump(ids, f, indent=4)