# -*- coding: utf-8 -*-
import logging
import os

FILE_PATH = "./logging_practise/log/log.log"


class LoggerFactory:
    __base_log: logging.Logger = None

    @classmethod
    def get_logger(cls, logger_name: str) -> logging.Logger:
        """
        Specify the logger_name to get the specific logger from its namcespace.

        Levels:
        [DEBUG, INFO, WARNING, ERROR, CRITICAL]
        [   10,   20,      30,    40,       50]
        """
        if cls.__base_log is None:
            cls._build()
        return cls.__base_log.getChild(logger_name)

    @classmethod
    def _build(
        cls,
        stream_level: int = logging.DEBUG,
        file_level: int = logging.ERROR,
        file_path: str = FILE_PATH,
    ) -> None:
        # create .log file with header
        cls._create_file(record_path=file_path)

        # build stream handler
        stream_handler = logging.StreamHandler()
        stream_formatter = logging.Formatter(
            fmt=(
                "[%(asctime)s], "
                "[%(filename)s], "
                "[%(funcName)s], "
                "[%(threadName)s], "
                "[%(levelname)s],\n"
                "%(message)s"
            )
        )
        stream_handler.setFormatter(stream_formatter)
        stream_handler.setLevel(stream_level)

        # build file handler
        file_handler = logging.FileHandler(file_path, mode="a+")
        file_format = logging.Formatter(
            fmt=(
                "[%(asctime)s], "
                "[%(filename)s], "
                "[%(funcName)s], "
                "[%(threadName)s], "
                "[%(levelname)s], "
                "%(message)s"
            )
        )
        file_handler.setFormatter(file_format)
        file_handler.setLevel(file_level)

        # setup custom root log
        root_logger = logging.getLogger("root")
        root_logger.setLevel(logging.DEBUG)
        root_logger.addHandler(stream_handler)
        root_logger.addHandler(file_handler)
        cls.__base_log = root_logger

    @classmethod
    def _create_file(cls, record_path: str) -> None:
        folder_path = os.path.dirname(record_path)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
