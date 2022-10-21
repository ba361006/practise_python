from gettext import gettext
from typing import Optional, Union

# class Hello1:
#     hello1 = 1

# class Hello2:
#     hello2 = 2

# def foo(bar: Union[Hello1, Hello2]):
#     print(
#         bar.hello1 # type: ignore
#     )


from dataclasses import dataclass


@dataclass
class Hello:
    name: Optional[str]


def hello(name: str):
    print(name)


a = Hello(name="name")
hello(name=a.name)
