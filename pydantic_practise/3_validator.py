from pydantic import BaseModel, ValidationError, validator


class UserModel(BaseModel):
    # order matters here for calling values in validator
    name: str
    username: str
    password1: str
    password2: str

    @validator('name')
    def name_must_contain_space(cls, v):
        # validator is a classmethod, and the second argument will be the focusing field
        # which is name in this case
        if ' ' not in v:
            raise ValueError('must contain a space')
        return v.title()

    @validator('password2')
    def passwords_match(cls, v, values, **kwargs):
        # this function focuses on password2, and values is a keyword for validator
        # values will return any "previous" validated fields which will be name, username and password1
        # you can switch the order of password1 and password2 and try run the code again to see the result
        print("values: ", values)
        if 'password1' in values and v != values['password1']:
            raise ValueError('passwords do not match')
        return v

    @validator('username')
    def username_alphanumeric(cls, v):
        assert v.isalnum(), 'must be alphanumeric'
        return v


user = UserModel(
    name='samuel colvin',
    username='scolvin',
    password1='zxcvbn',
    password2='zxcvbn',
)
print(user)