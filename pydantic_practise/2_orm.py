import pydantic


class NormalSample:
    def __init__(self, name: str):
        self.name = name
    
class PydanticSample(pydantic.BaseModel):
    name: str

class OrmModel(pydantic.BaseModel):
    name: str
    
    class Config():
        orm_mode = True
        

def parse_obj(sample):
    new_model = OrmModel.parse_obj(sample)
    print(f"parse_obj: object={sample.__class__}, object.name={new_model.name}")
    
def from_orm(sample):
    new_model =OrmModel.from_orm(sample)
    print(f"from_orm: object={sample.__class__}, object.name={new_model.name}")

if __name__ == "__main__":
    normal_sample = NormalSample(name="hello")
    pydantic_sample = PydanticSample(name="hello")
    
    # normal_sample will fail since parse_obj can only parse pydantic model
    try:
        parse_obj(sample=normal_sample)
    except Exception as err:
        print(err)
    parse_obj(sample=pydantic_sample)
    
    # both work
    print()
    from_orm(sample=normal_sample)
    from_orm(sample=pydantic_sample)
    