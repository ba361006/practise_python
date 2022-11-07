# -*- coding: utf-8 -*-
import asyncio
import functools
import inspect
import logging
from types import FrameType
from typing import Any
from typing import Callable
from typing import cast
from typing import Optional
from typing import TypeVar

import aioredis
import async_timeout
from redis import asyncio as aioredis
from redis.asyncio import Redis

TIMEOUT = 1
setting_url = "redis://localhost"

APPLOG = logging.getLogger(__name__)

FnT = TypeVar("FnT", bound=Callable[..., Any])


class RedisError:
    pass


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
            caller_func_name = inspect.currentframe()
            if isinstance(caller_func_name, FrameType):
                caller_func_name = caller_func_name.f_code.co_name  # type:ignore
            APPLOG.warning(
                "Error while calling %s from %s: %s",
                func.__name__,
                caller_func_name,
                err,
            )
            return RedisError

    return cast(FnT, wrapper)


class RedisCache:
    @redis_timeout
    async def task_1(redis: Optional[Redis] = None) -> None:
        await redis.set(name="happy", value="sym")  # type: ignore
        return await redis.get("happy")  # type: ignore


async def main():
    response = await RedisCache.task_1()
    if response is RedisError:
        print("Hello")
    print("task1: ", response.decode("utf-8"))


if __name__ == "__main__":
    asyncio.run(main())
