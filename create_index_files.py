import os
import json
from typing import List

def get_channel_folders() -> List[str]:
    entries = os.scandir(".")
    return [entry.name for entry in entries if entry.is_dir()]

def get_json_file_list(folder: str) -> List[str]:
    entries = os.scandir(folder)
    return [entry.name for entry in entries if entry.name.endswith(".json") and entry.name != "index.json"]

def create_index_file(folder: str, files: List[str]) -> None:
    filepath = os.path.join(folder, "index.json")
    with open(filepath, "w") as f:
        json.dump(files, f, indent=2)

def main() -> None:
    channel_folders = get_channel_folders()
    for folder in channel_folders:
        json_files = get_json_file_list(folder)
        create_index_file(folder, json_files)

if __name__ == "__main__":
    main()
