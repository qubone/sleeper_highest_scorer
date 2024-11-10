"""Handling of shared functions."""

import json
from pathlib import Path
from typing import Dict, Any
import requests


def http_get_response_data_text(url: str) -> Dict[str, Any]:
    """Returns HTTP GET in text format.
    """
    response = requests.get(url, timeout=10)
    return json.loads(response.text)


def http_get_response_data_json(url: str) -> Dict[str, Any] | None:
    """Returns HTTP GET in JSON format.
    """
    response = requests.get(url, timeout=None)
    return response.json() if response.status_code == 200 else None


def write_json_to_file(data: dict, output_file: str):
    """Helper function to write JSON data to file.
    """
    with open(output_file, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def read_json_from_file(input_file: Path) -> Dict[str, Any]:
    """Helper function to read JSON data from file.
    """
    if not input_file.exists():
        raise FileNotFoundError
    with open(input_file, "r", encoding="utf-8") as file:
        return json.load(file)
