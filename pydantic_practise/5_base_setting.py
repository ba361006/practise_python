# -*- coding: utf-8 -*-
import pydantic


class Setting(pydantic.BaseSettings):
    # pick one of your environment variable
    CORSA_API: str = "default"
    non_env_variable: str = "hello"


if __name__ == "__main__":
    """
    environment variable will be assigned to class variable if it's found,
    otherwise default value defined under the class will be printed
    """
    setting = Setting()
    print("env_variable: ", setting.CORSA_API)
    print("non_env_variable: ", setting.non_env_variable)
