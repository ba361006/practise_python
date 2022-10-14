from typing import Any

import aioredis
import async_timeout
import asyncio
import functools
from aioredis import ConnectionsPool


def timeout_decorator(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            async with async_timeout.timeout(0.5):
                return await func(*args, **kwargs)
        except asyncio.exceptions.TimeoutError:
            print("RedisCache has reached %s seconds", 0.5)
            raise
        except Exception as err:
            print("RedisCache error: %s", err)
            raise
    return wrapper

class RedisCache:
    redis: ConnectionsPool


    async def connect(self) -> None:
        self.redis = await aioredis.create_redis_pool("redis://localhost")

    async def set(self, key: str, value: str) -> Any:
        return await self.redis.set(key, value)

    async def get(self, key: str) -> Any:
        return await self.redis.get(key)

    async def expire(self, key: str, timeout: int) -> Any:
        return await self.redis.expire(key, timeout)

    async def flushall(self) -> Any:
        return await self.redis.flushall()

    async def delete(self, key: str) -> Any:
        return await self.redis.delete(key)

    def close(self) -> None:
        self.redis.close()

    @timeout_decorator
    async def test(self, key, value):
        # raise ValueError
        await asyncio.sleep(1)
        await self.set(key, value)
        response = await self.get(key)
        print(response)

async def main():
    cache = RedisCache()
    await cache.connect()
    await cache.test("hello", "world")

if __name__ == "__main__":
    asyncio.run(main())


