# Synchronous approach

# You:

# Take Order A
# Give it to kitchen
# Stand there and wait
# Food is ready
# Serve A
# Take Order B
# Repeat

# The waiter is doing nothing while the kitchen is working.

# Take Order A
# Give it to kitchen
# While A is cooking → take Order B
# While B is cooking → take Order C
# Serve whichever is ready

# Task A ────────────────>
#                        WAIT
#                        WAIT
#                        WAIT
# Task B ────────────────>

# Task A ────────┐
#                │ waiting
# Task B ────┐   │
#            │   │
# Task C ────┼───┘
#            │
#         Event Loop
#            │
#       switch between
#         ready tasks


# API calls
#    ↓
# Database queries
#    ↓
# HTTP requests
#    ↓
# File I/O
#    ↓
# Web scraping
#    ↓
# Network sockets


    #         EVENT LOOP
    #              │
    #    ┌─────────┼─────────┐
    #    ↓         ↓         ↓
    # Task A     Task B    Task C
    #    │         │         │
    # waiting    ready     waiting
    #    │         ↓         │
    #    └──── Event Loop ───┘


import asyncio


# async def hello():
#     print("Hello")

# result = hello()

# print(result)



# async def hello()
#        │
#        ↓
#  coroutine function
#        │
#        │ hello()
#        ↓
#  coroutine object
#        │
#        │ await
#        ↓
#  actually execute


async def hello():
    print("Hello 123")
    await asyncio.sleep(1) # timer.sleep(1) # Block the thread.
    # Pause this coroutine and give the event loop a chance to do other work.
    print("Hello")

# result = hello()

# print(result)


asyncio.run(hello()) # Create the event loop → run main() → finish → clean up

# asyncio.run(main())
#         │
#         ↓
#    Event Loop
#         │
#         ↓
#      main()
#         │
#         ↓
#      await...
#         │
#         ↓
#      result
#         │
#         ↓
#     loop closes


async def download(name, seconds):
    print(f"{name} started")

    await asyncio.sleep(seconds)

    print(f"{name} completed")


async def main():
    await download("File A", 2)
    await download("File B", 2)


asyncio.run(main())


async def main():

    task1 = asyncio.create_task( # Start Work Concurrently
        download("File A", 2)
    )

    task2 = asyncio.create_task(
        download("File B", 2)
    )

    await task1
    await task2

asyncio.run(main())


