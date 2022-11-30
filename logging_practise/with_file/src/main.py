# -*- coding: utf-8 -*-
import logging
import os
from logging.config import fileConfig

import setting
from bar import bar
from foo import foo


def main():
    fileConfig(os.path.join(os.path.dirname(os.path.abspath(__file__)), "logger.ini"))

    # root level is warning so logging.info will neither be printed nor saving to log file
    logging.info(f"name: {__name__}, logger_name: root")
    logging.warning(f"name: {__name__}, logger_name: root")

    # loggers in both setting and bar have not listed in logger.ini, so it will inherit root logger
    setting.debug_from_setting()
    bar.debug_from_bar()

    # foo is defined in logger.ini, so it will follow the config under [logger_foo]
    foo.debug_from_foo()


if __name__ == "__main__":
    # go check README for futher info
    main()
