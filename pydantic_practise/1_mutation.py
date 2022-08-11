import pydantic
from enum import Enum


class Color(Enum):
    __contents = {
        "Eng":{
            "red":"red",
            "blue":"blue"
        },
        "Chi":{
            "red":"紅",
            "blue":"藍"
        }
    }
    red:str
    blue:str

    @classmethod
    def make_example(cls, language="Eng"):
        translate_dict = cls.__contents.value
        for key, value in translate_dict[language].items():
            setattr(cls, key, value)
        return cls

class Test(pydantic.BaseModel):
    class Config:
        allow_mutation = False
    colour = Color

    @classmethod
    def make_example(cls, language="Eng"):
        Color.make_example(language=language)


test = Test()
test.make_example(language="Eng")
print(id(test.colour))
print(test.colour.red)
print(test.colour.blue)

print()

test.make_example(language="Chi")
print(id(test.colour))
test.colour.red=1
print(test.colour.red)
print(test.colour.blue)





# class Immutable(pydantic.BaseModel):
#     class Config:
#         allow_mutation = False

# class OSCheck(Immutable):
#     window_title: str
#     hello: str

#     @classmethod
#     def make_example(cls, language:str = "English"):
#         contents = {
#             "English":{
#                 "window_title": "OSCheck"
#             },
#             "Chinese":{
#                 "window_title": "作業系統檢測"
#             }
#         }
#         cls.window_title = contents[language]
#         for i in cls:
#             print(i)


# class Duplicate(Immutable):
#     window_title: str
#     @classmethod
#     def make_example(cls, language:str = "English"):
#         contents = {
#             "English":{
#                 "window_title": "OSCheck"
#             },
#             "Chinese":{
#                 "window_title": "作業系統檢測"
#             }
#         }
#         cls.window_title = contents[language]["window_title"]

# class Translator:
#     os_check = OSCheck(window_title="1", hello="2")
#     # duplicate = Duplicate()

#     @classmethod
#     def make_example(cls, language:str = "English"):
#         cls.os_check.make_example(language=language)
#         # cls.duplicate.make_example(language=language)

# translator = Translator()
# translator.make_example(language="English")

# # print(translator.os_check.window_title)