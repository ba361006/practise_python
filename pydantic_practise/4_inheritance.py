import pydantic
import typing
from datetime import datetime, date

# datetime is the subclass of date
print(issubclass(datetime, date))

class Test(pydantic.BaseModel):
    # time can receive date
    date_only: typing.Union[None, date]
    date_and_datetime: typing.Union[None, datetime, date]
    
    
    # since datetime is the subclass of date, assign datetime to the type annotation of v works
    # and None also works since Optional accepts either None or the given type
    @pydantic.validator("date_only")
    def check_date_only(cls, v: typing.Optional[datetime]):
        print("check_date_only: " , v)
        return v
        
    # it also works since v accepts either None or datetime, and datetime is the subclass of date
    # so either None or datetime works, but if datetime is given
    @pydantic.validator("date_and_datetime")
    def check_date_and_datetime(cls, v: typing.Optional[datetime]):
        print("check_date_and_datetime: ", v)
        return v


print()
test = Test(date_only=None, date_and_datetime=None)

print()
test = Test(date_only=datetime.now(), date_and_datetime=datetime.now())

print()
test = Test(date_only=date(2022,8,24), date_and_datetime=date(2022,8,24))