import asyncio

async def download(name, seconds):
    print(f"{name} started")

    await asyncio.sleep(seconds)

    print(f"{name} completed")
    return name

async def main():
    results = await asyncio.gather(
        download("A", 2),
        download("B", 2),
        download("C", 1),
        return_exceptions=True
    )
    print(results)

asyncio.run(main())


# return_exceptions=True is useful for batch-style independent work where one failure 
# should not automatically hide the outcomes of other tasks.

# done, pending = await asyncio.wait(
#     tasks
# )

# async with asyncio.timeout(3):

#     await some_operation()


async def fetch_data():
    await asyncio.sleep(5)
    return "data"


async def main():

    try:
        async with asyncio.timeout(3):
            result = await fetch_data()

            print(result)

    except TimeoutError:
        print("Operation timed out")



async def main():

    async with asyncio.TaskGroup() as group:

        group.create_task(download("A", 2))
        group.create_task(download("B", 1))
        group.create_task(download("C", 3))


# TaskGroup = Put related tasks inside one managed group.


# asyncio.Queue

# queue = asyncio.Queue()

# await queue.put("job-1")

# job = await queue.get()

# print(job)

# queue.task_done()

# asyncio.Event

# asyncio.Lock

# asyncio.Semaphore


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


# Don't create a new HTTP session for every request.
# and reuse the session for multiple requests.