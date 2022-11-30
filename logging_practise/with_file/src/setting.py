# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger(__name__)


def hello_from_setting():
    logger.debug(f"name: {__name__}, logger_name: {logger.name}")
