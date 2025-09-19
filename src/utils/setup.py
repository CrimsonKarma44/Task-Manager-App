import os
import json
from dotenv import load_dotenv

from pathlib import Path

def ensure_json_file(filepath: str) -> None:
    """Ensure the JSON file exists, creating directory if needed."""
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not path.exists():
        path.write_text(json.dumps([]))  # <-- Fix: initialize with empty list

def read_json_file(filepath: str) -> list:
    """Read the JSON file and return its contents as a list."""
    ensure_json_file(filepath)
    with open(filepath, 'r') as f:
        return json.load(f)

def write_json_file(filepath: os.path, data) -> None:
    """Write a dictionary to the JSON file."""
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

def load_config() -> str:
    # Load variables from .env into environment
    load_dotenv()

    # Get the STORAGE_FILE variable
    storage_file = os.getenv("STORAGE_FILE")

    if not storage_file:
        raise ValueError("STORAGE_FILE not set in .env")

    return storage_file

if __name__ == "__main__":
    storage_file = load_config()
    print(f"Using storage file: {storage_file}")
    ensure_json_file(storage_file)
    data = read_json_file(storage_file)
    print(f"Current data in {storage_file}: {data}")
    # Example of writing data
    new_data = {"example_key": "example_value"}
    write_json_file(storage_file, new_data)
    print(f"Updated data in {storage_file}: {read_json_file(storage_file)}")