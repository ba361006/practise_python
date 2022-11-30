# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger(__name__)


def debug_from_foo():
    logger.debug(f"name: {__name__}, logger_name: {logger.name}")
