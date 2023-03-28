import html
import logging
import requests

from ..config import settings

logger = logging.getLogger(__name__)


class FetchProgramException(Exception):
    pass


def get_current_programme():
    url = settings["inputs.openwebif.url"]
    service_ref = _get_service(url)
    title, summary = _get_epg_now_next(url, service_ref)
    logger.info(f"openwebif url={url} title={title} summary={summary}")
    return title, summary


def _get_service(url: str):
    r = requests.get(f"{url}/api/epgnownext?bRef=0")
    now_next = r.json()
    return now_next["info"]["ref"]


def _get_epg_now_next(url: str, service_ref: str):
    r = requests.get(f"{url}/api/epgservicenow?sRef={service_ref}")
    service_now = r.json()
    epg_now = service_now["events"][0]
    epg_title = html.unescape(epg_now["title"])
    epg_summary = html.unescape(epg_now["shortdesc"])
    return epg_title, epg_summary
