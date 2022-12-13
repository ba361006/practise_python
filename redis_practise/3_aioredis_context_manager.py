# -*- coding: utf-8 -*-
from __future__ import annotations

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
                return await func(*args, **kwargs)
        except asyncio.exceptions.TimeoutError:
            APPLOG.error("RedisCache has reached %s seconds", TIMEOUT)
        except Exception as err:  # pylint: disable=broad-except
            APPLOG.error(
                "RedisCache error while calling cache.%s: %s",
                func.__name__,
                err,
            )

    return cast(FnT, wrapper)


class RedisCache:
    """
    while redis server is disconnected, aioredis.from_url still returns Redis
    and will raise an exception when redis action is invoked.
    then, @redis_timeout will handle the error and return None
    so the flow should work as normal
    """

    async def __aenter__(self) -> RedisCache:
        # pylint: disable=attribute-defined-outside-init
        # __aenter__ isn't decorated with @redis_timeout
        # since we need to return self to let the flow fly as normal
        try:
            async with async_timeout.timeout(TIMEOUT):
                self._redis: Redis = await aioredis.from_url(setting_url)
        except asyncio.exceptions.TimeoutError:
            APPLOG.error("RedisCache has reached %s seconds", TIMEOUT)
        except Exception as err:  # pylint: disable=broad-except
            APPLOG.error("RedisCache context manager error: %s", err)
        return self

    @redis_timeout
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._redis.close()

    @redis_timeout
    async def action(self) -> None:
        await self._redis.set(name="happy", value="sym")  # type: ignore
        return await self._redis.get("happy")  # type: ignore


async def main():
    async with RedisCache() as redis:
        print("redis_action: ", await redis.action())
        print("do something")


if __name__ == "__main__":
    asyncio.run(main())
