# -*- coding: utf-8 -*-
import threading

from feature.feature import hello
from handler.logging import LoggerFactory

logger = LoggerFactory.get_logger(__name__)


def main():
    logger.error("hello")
    thread = threading.Thread(target=hello)
    thread.start()
    thread.join()


if __name__ == "__main__":
    main()
