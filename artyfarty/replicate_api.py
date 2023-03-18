from .config import settings
import datetime
import logging
import os
import replicate
import requests
from typing import Optional

logger = logging.getLogger(__name__)


def clean_prompt(input: str):
    cleaned = "".join(char for char in input.lower() if char.isalnum() or char in [" "])
    return cleaned.replace(" ", "_")


def fetch_file(url: str, dest: str):
    r = requests.get(url, allow_redirects=True)
    open(dest, "wb").write(r.content)


def call_api(
    prompt: str = "",
    negative: Optional[str] = None,
    prefix: Optional[str] = None,
    suffix: Optional[str] = None,
):
    model_name = settings["replicate.model"]
    model_version = settings["replicate.model_version"]
    prompt_negative = negative or settings["replicate.prompt_negative"]
    prompt_prefix = prefix or settings["replicate.prompt_prefix"]
    prompt_suffix = suffix or settings["replicate.prompt_suffix"]
    client = replicate.Client(api_token=settings["replicate_api_token"])
    model = client.models.get(model_name)
    version = model.versions.get(model_version)
    prompt_full = f"{prompt_prefix}, {prompt}, {prompt_suffix}".strip()
    prompt_filename = clean_prompt(prompt_full)
    inputs = dict(
        prompt=prompt_full,
        negative_prompt=prompt_negative,
        width=settings["replicate.output.width"],
        height=settings["replicate.output.height"],
    )
    out = version.predict(**inputs)
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")

    filename = now.strftime("%Y-%m-%d_%H-%M-%S")
    dest = os.path.join(settings["output_dir"], f"{timestamp}_{prompt_filename}.png")
    logger.info(
        f"model={model_name} version={model_version} inputs={inputs} dest={dest}"
    )
    fetch_file(out[0], dest)
