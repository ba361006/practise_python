"""
before running this script, please make sure your redis server is running
check README.md for further information
"""

import aioredis
import asyncio


async def single_set(service: aioredis.Redis) -> None:
    print()
    print("### single set ###")
    await service.set(name="hello", value="world")
    
    # this will return bytes instead by default
    response = await service.get(name="hello")
    print(response, response.__class__)

    # to convert bytes to str
    response = await service.get(name="hello")
    response = response.decode("utf-8")
    print(response, response.__class__)
    

async def multiple_set(service: aioredis.Redis) -> None:
    print()
    print("### multiple set ###")
    await service.mset(mapping={"hello1": "world1", "hello2": "world2"})
    response = await service.mget(keys=["hello1", "hello2", "wrong_key"])
    print(response)

async def main(service: aioredis.Redis):
    await single_set(service=service)
    await multiple_set(service=service)

if __name__ == "__main__":
    # TCP socket connection and reuse is done behind the scenes after invoking redis.Redis()
    # default port will be 6379
    redis_service = aioredis.from_url("redis://localhost")
    asyncio.run(main(service=redis_service))

    