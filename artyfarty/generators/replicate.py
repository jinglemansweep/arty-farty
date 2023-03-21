from ..config import settings
import logging
import replicate


logger = logging.getLogger(__name__)


def generate_image(model: str, version: str, inputs: dict) -> str:
    client = replicate.Client(api_token=settings["replicate_api_token"])
    model_inst = client.models.get(model)
    model_version = model_inst.versions.get(version)
    logger.info(f"replicate:generate model={model} version={version} inputs={inputs}")
    out = model_version.predict(**inputs)
    return out[0]
