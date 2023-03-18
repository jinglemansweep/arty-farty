import html
import logging
import requests

from ..config import settings

logger = logging.getLogger(__name__)


def run():
    logger.info("OpenWEBIF")
    return get_epg_now()


def get_epg_now():
    try:
        url = settings["inputs.openwebif.url"]
        r = requests.get(f"{url}/api/epgnownext?bRef=0")
        now_next = r.json()
        service_ref = now_next["info"]["ref"]
        r = requests.get(f"{url}/api/epgservicenow?sRef={service_ref}")
        service_now = r.json()
        epg_now = service_now["events"][0]
        epg_title = html.unescape(epg_now["title"])
        epg_summary = html.unescape(epg_now["shortdesc"])
    except Exception as e:
        logger.error("Error", exc_info=e)
        return None
    finally:
        return epg_title, epg_summary
