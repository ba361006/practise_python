# -*- coding: utf-8 -*-
import asyncio
import functools
import logging
from typing import Any
from typing import Callable
from typing import cast
from typing import TypeVar

import aioredis
import async_timeout
from redis import asyncio as aioredis
from redis.asyncio import Redis

TIMEOUT = 1
setting_url = "redis://localhost"

APPLOG = logging.getLogger(__name__)

FnT = TypeVar("FnT", bound=Callable[..., Any])


def redis_timeout(func: FnT) -> FnT:
    @functools.wraps(func)
    async def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            async with async_timeout.timeout(TIMEOUT):
                async with aioredis.from_url(setting_url) as redis:
                    return await func(*args, **kwargs, redis=redis)
        except asyncio.exceptions.TimeoutError:
            APPLOG.error("RedisCache has reached %s seconds", TIMEOUT)
        except Exception as err:
            APPLOG.error("RedisCache error: %s", err)
            raise

    return cast(FnT, wrapper)


class RedisCache:
    @redis_timeout
    async def task_1(self, redis) -> None:
        await redis.set(name="happy", value="sym")
        response = await redis.get("happy")
        print(response.decode("utf-8"))


async def main():
    cache = RedisCache()
    await cache.task_1()


if __name__ == "__main__":
    asyncio.run(main())
