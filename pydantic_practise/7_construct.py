# -*- coding: utf-8 -*-
import typing

import pydantic


class TestModel(pydantic.BaseModel):
    test_list: typing.List[int]

    @pydantic.validator("test_list")
    def validate(cls, list) -> None:
        if len(list) == 0:
            raise ValueError("Bitch")


def main():
    try:
        TestModel(test_list=[])
    except Exception as err:
        print("Instantiate the TestModel with empty list will not pass the validator")
    print()

    a = TestModel.construct(test_list=[])
    print("Construct the TestModel with will ignore the validator: ", a.test_list)


if __name__ == "__main__":
    main()
