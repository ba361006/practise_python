# -*- coding: utf-8 -*-
from __future__ import annotations

import asyncio
import functools
import inspect
import logging
from types import FrameType
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
    @redis_timeout
    async def __aenter__(self) -> RedisCache:
        # pylint: disable=attribute-defined-outside-init
        self.redis: Redis = await aioredis.from_url(setting_url)
        return self

    @redis_timeout
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.redis.close()

    @redis_timeout
    async def action(self) -> None:
        await self.redis.set(name="happy", value="sym")  # type: ignore
        return await self.redis.get("happy")  # type: ignore


async def main():
    async with RedisCache() as redis:
        print("redis_action: ", await redis.action())
        print("do something")


if __name__ == "__main__":
    asyncio.run(main())
