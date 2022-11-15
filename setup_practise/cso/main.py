# -*- coding: utf-8 -*-
import pydantic


class Hello(pydantic.BaseModel):
    name: str


def main():
    hello = Hello(name="name")
    print(hello.name)


if __name__ == "__main__":
    main()
