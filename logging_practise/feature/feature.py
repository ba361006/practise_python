# -*- coding: utf-8 -*-
from handler.logging import LoggerFactory

logger = LoggerFactory.get_logger(__name__)


def hello():
    try:
        raise ValueError("bitch")
    except Exception as err:
        logger.exception("Hello from %s", err)
