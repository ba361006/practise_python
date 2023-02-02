# -*- coding: utf-8 -*-
import asyncio


async def loop(name: str, count_time: int):
    try:
        for i in range(count_time):
            print(f"{name} counts {i}")
            await asyncio.sleep(0.5)

            if name == "child" and i == 4:
                raise ValueError("child exception is raised")
    finally:
        print("# finally!!")


async def main() -> None:
    main_task = asyncio.create_task(loop("main", 10))

    async_loop = asyncio.get_running_loop()

    task = async_loop.create_task(loop("child", 6))

    try:
        await task
    except Exception as err:
        print(
            "# exception will happen at where it is awaited, not where it is created: ",
            err,
        )
    await main_task


if __name__ == "__main__":
    asyncio.run(main())
