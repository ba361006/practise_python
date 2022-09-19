import asyncio


async def loop(name: str, count_time: int):
    for i in range(count_time):
        print(f"{name} counts {i}")
        await asyncio.sleep(0.5)
    
async def hello():
    print("hello!")

async def main():
    created_task = asyncio.create_task(loop("created_task", 4))
    normal_task = loop("normal_task", 2)
    
    # # this order works linearly though both of them are async function
    # await created_task
    # await normal_task
    
    # this one works concurrently since the point of switching tasks is await
    # firstly, asyncio.create_task creates and schedules the given awaitable task to the event loop
    # and get ready to be executed as soon as the current corroutine gives the control back to event loop
    # secondly, normal_task is submitted to the event loop via await 
    # at this stage, there are two functions in the event loop. Both of them will be executed
    # and give control back to event loop while it meet await 
    # so we will see the message printing out asynchronously
    await normal_task
    await created_task
    # for the main function, it does work linearly, so we will see the "finish!" 
    # after normal_task and created_task are done
    print("finish!")

if __name__ == "__main__":
    asyncio.run(main())
    