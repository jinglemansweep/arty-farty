import logging
from pprint import pprint
from .config import settings
from .replicate_api import call_api
from .inputs import openwebif

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

title, summary = openwebif.run()

logger.info(f"OPENWEBIF title={title} summary={summary}")

call_api(summary)
