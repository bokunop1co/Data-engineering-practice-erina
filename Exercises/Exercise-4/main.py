import glob
import json
import csv
import os


def flatten(data, parent_key="", sep="_"):
    # Aplana un diccionario anidado (dicts y listas) en un solo nivel.
    items = {}
    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.update(flatten(value, new_key, sep=sep))
        elif isinstance(value, list):
            for i, item in enumerate(value):
                items[f"{new_key}_{i}"] = item
        else:
            items[new_key] = value
    return items


def main():
    json_files = glob.glob("data/**/*.json", recursive=True)

    for path in json_files:
        with open(path) as f:
            data = json.load(f)
        flat = flatten(data)

        csv_path = os.path.splitext(path)[0] + ".csv"
        with open(csv_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=flat.keys())
            writer.writeheader()
            writer.writerow(flat)


if __name__ == "__main__":
    main()
