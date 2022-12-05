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


def redis_action_error(func: FnT) -> FnT:
    @functools.wraps(func)
    async def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return await func(*args, **kwargs)
        except Exception as err:  # pylint: disable=broad-except
            caller_func_name = inspect.currentframe()
            if isinstance(caller_func_name, FrameType):
                caller_func_name = caller_func_name.f_code.co_name  # type: ignore
            APPLOG.error(
                "RedisCache error while calling cache.%s from %s: %s",
                func.__name__,
                caller_func_name,
                err,
            )

    return cast(FnT, wrapper)


class RedisCache:
    async def __aenter__(self) -> RedisClient:
        try:
            async with async_timeout.timeout(TIMEOUT):
                redis = await aioredis.from_url(setting_url)
                await asyncio.sleep(2)
                return RedisClient(redis)
        except asyncio.exceptions.TimeoutError:
            APPLOG.error("RedisCache has reached %s seconds", TIMEOUT)

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Do nothing here to let the flow work normally"""


class RedisClient:
    def __init__(self, redis):
        self.redis = redis

    @redis_action_error
    async def action(self) -> None:
        await self.redis.set(name="happy", value="sym")  # type: ignore
        return await self.redis.get("happy")  # type: ignore


async def main():
    async with RedisCache() as redis_client:
        response = await redis_client.action()
        if response:
            print("task1: ", response.decode("utf-8"))
        else:
            print("response: ", response)


if __name__ == "__main__":
    asyncio.run(main())
