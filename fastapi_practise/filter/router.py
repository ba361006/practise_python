import qurey_rule
import fastapi
import sqlalchemy
from sqlalchemy.dialects.postgresql import INET
router = fastapi.APIRouter()

class Subnet:
    name = sqlalchemy.Column(sqlalchemy.VARCHAR(45))
    subnet_cidr = sqlalchemy.Column(sqlalchemy.ARRAY(INET))
    start_ip = sqlalchemy.Column(sqlalchemy.ARRAY(INET))
    end_ip = sqlalchemy.Column(sqlalchemy.ARRAY(INET))
    gateway_ip = sqlalchemy.Column(sqlalchemy.ARRAY(INET))
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, nullable=True)

class SubnetRule(qurey_rule.QueryRule):
    name = qurey_rule.FilterLike.new_class(Subnet.name) 
    subnet_cidr = qurey_rule.FilterEqual.new_class(Subnet.subnet_cidr) 
    start_ip = qurey_rule.FilterEqual.new_class(Subnet.start_ip) 
    end_ip = qurey_rule.FilterEqual.new_class(Subnet.end_ip) 
    gateway_ip = qurey_rule.FilterEqual.new_class(Subnet.gateway_ip) 
    created_at = qurey_rule.FilterEqual.new_class(Subnet.created_at) # TBD


@router.get(
    "/",
    responses={404: {"description": "Not Found"}, 503: {}}
)
async def root(query: qurey_rule.QueryRule = fastapi.Depends(qurey_rule.QueryRule.parse)):
    return {"query": str(query)}


# # uvicorn router:router --reload
