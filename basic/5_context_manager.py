# -*- coding: utf-8 -*-
import asyncio


class Context:
    def __enter__(self) -> str:
        """interrupt the flow if any exception happens here"""
        return "Get in __enter__"

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        """flow goes here if any exception happens under the context manager's scope"""
        print("exc_type: ", exc_type)
        print("exc_val: ", exc_val)
        print("exc_tb: ", exc_tb)

        # return anything to ignore the exception and continue the normal execution
        return True


class AsyncContext:
    async def __aenter__(self) -> str:
        """interrupt the flow if any exception happens here"""
        return "Get in __aenter__"

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> bool:
        """flow goes here if any exception happens under the context manager's scope"""
        print("exc_type: ", exc_type)
        print("exc_val: ", exc_val)
        print("exc_tb: ", exc_tb)

        # return anything to ignore the exception and continue the normal execution
        return True


async def main():
    print("Context manager")
    with Context() as context:
        print(context)
        raise ValueError("exception happens")

    print()
    print("AsyncContext manager")
    async with AsyncContext() as context:
        print(context)
        raise ValueError("exception happens")


if __name__ == "__main__":
    asyncio.run(main())
