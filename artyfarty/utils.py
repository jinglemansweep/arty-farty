import os
import yaml
import requests
from datetime import datetime
from typing import Optional


def build_output_filename(
    prompt: str, timestamp: bool = False, prefix: Optional[str] = None
) -> str:
    prompt_safe = convert_safe_filename(prompt)
    prefix_str = ""
    if prefix is not None:
        prefix_str = prefix + "_"
    timestamp_str = ""
    if timestamp:
        now = datetime.now()
        timestamp_str = now.strftime("%Y%m%d%H%M%S") + "_"
    return f"{prefix_str}{timestamp_str}{prompt_safe}"


def get_file_extension(filename: str) -> str:
    return os.path.splitext(os.path.basename(filename))[1]


def convert_safe_filename(input: str) -> str:
    cleaned = "".join(char for char in input.lower() if char.isalnum() or char in [" "])
    return cleaned.replace(" ", "_")


def download_file(url: str, output_file: str) -> None:
    r = requests.get(url, allow_redirects=True)
    open(output_file, "wb").write(r.content)


def write_metadata_file(data: dict, output_file: str) -> None:
    with open(output_file, "w") as outfile:
        yaml.dump(data, outfile, default_flow_style=False)
