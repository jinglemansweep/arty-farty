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
    "In the style of Picasso",
    "In the style of Tron",
    "In the style of a Disney movie",
    "In the styke of the Matrix",
]
suffixes = ["output in mono", "output in sepia", "output in halftone effect"]

call_api(summary, prefix=random.choice(prefixes), suffix=random.choice(suffixes))
