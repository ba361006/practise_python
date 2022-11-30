# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger(__name__)


def hello_from_bar():
    logging.warning(f"name: {__name__}, logger_name: {logger.name}")
    logger.debug(f"name: {__name__}, logger_name: {logger.name}")
