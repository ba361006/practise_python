import pydantic
from datetime import datetime
from typing import List, Optional

class User(pydantic.BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []
    # the first arg will be seens as the default value
    # for parents. Ellipsis(...) indicates the feild is required
    # check the Field function docstring for further information
    parents: str = pydantic.Field(...)
    

user = User(
    id=123, 
    signup_ts=datetime.now(), 
    friends=[1,2,3,4],
    parents="dad & mom"
)
print(user.id)

# field can be reassigned
user.id = 321
print(user.id)