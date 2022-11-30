# -*- coding: utf-8 -*-
import logging
import os
from logging.config import fileConfig

import setting
from bar import bar
from foo import foo

logger = logging.getLogger(__name__)


def main():
    fileConfig(os.path.join(os.path.dirname(os.path.abspath(__file__)), "logger.ini"))
    logging.debug(f"name: {__name__}, logger_name: {logger.name}")
    logging.warning(f"name: {__name__}, logger_name: {logger.name}")
    logger.error(f"name: {__name__}, logger_name: {logger.name}")

    setting.hello_from_setting()
    bar.hello_from_bar()
    foo.hello_from_foo()


if __name__ == "__main__":
    # go check readme for futher info
    main()
