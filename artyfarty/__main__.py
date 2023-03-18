import logging
import random
from pprint import pprint
from .config import settings
from .replicate_api import call_api
from .inputs import openwebif

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

title, summary = openwebif.run()

logger.info(f"OPENWEBIF title={title} summary={summary}")

prefixes = [
    "",
]
suffixes = [
    "Monochrome Output.",
    "In style of Disney.",
    "In style of Picasso.",
    "In style of Tron.",
    "Set in the Future.",
    "In Pixel Art style.",
    "In style of Hollywood billboard.",
    "In style of fast food restaurant.",
]

call_api(summary, prefix=random.choice(prefixes), suffix=random.choice(suffixes))
