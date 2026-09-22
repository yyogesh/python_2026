# Student 1 → Download image
# Student 2 → Download image
# Student 3 → Download image
# Student 4 → Download image


# Download 1 → wait → finish
# Download 2 → wait → finish
# Download 3 → wait → finish
# Download 4 → wait → finish

# Download 1 ────────┐
# Download 2 ────────┤
# Download 3 ────────┤ → Finish
# Download 4 ────────┘

# Concurrency: Managing multiple tasks that make progress together

# Parallelism: Managing multiple tasks that run at the same time


# Threading : I/O bound : Multiple threads running at the same time
# Multiprocessing: CPU bound: Multiple processes running at the same time
# Asyncio: I/O bound: Cooperative tasks in one thread


    #                 Python Concurrency
    #                        │
    #       ┌────────────────┼────────────────┐
    #       ↓                ↓                ↓
    #   Threading       Multiprocessing     Asyncio
    #       │                │                │
    #    Waiting           Computing        Waiting
    #       │                │                │
    #    I/O-bound        CPU-bound        I/O-bound


# Downloading 100 files
#         ↓
#      Threading

# Resizing 100,000 images
#         ↓
#   Multiprocessing

# Calling 1,000 APIs
#         ↓
#       Asyncio


# GIL : Global Interpreter Lock
# Only one thread executes Python bytecode at a time within a process.


# Process
# │
# ├── Thread 1 ── 🔒
# ├── Thread 2 ── waiting
# ├── Thread 3 ── waiting
# └── Thread 4 ── waiting

# Thread 1
#    ↓
# API request
#    ↓
# WAITING................
#              ↓
#         Thread 2 works

# The program can make progress on other tasks while the first task waits.


# The GIL discussion is specifically about standard CPython builds with the GIL. 
# Python also has experimental/free-threaded builds in newer versions, but students should 
# still learn the traditional I/O → threads, CPU → processes model because it remains highly 
# relevant to ordinary CPython applications.



# import time

# def work(name):
#     print(f"{name} started")
#     time.sleep(2)
#     print(f"{name} finished")


# work("Task 1")
# work("Task 2")
# work("Task 3")


import threading
import time


def work(name):
    print(f"{name} started")
    time.sleep(2)
    print(f"{name} finished")


t1 = threading.Thread(target=work, args=("Task 1",))
t2 = threading.Thread(target=work, args=("Task 2",))
t3 = threading.Thread(target=work, args=("Task 3",))

t1.start()
t2.start()
t3.start()

t1.join() # Wait for this thread to finish.
t2.join()
t3.join()


balance = 100

balance += 10

# 120



counter = 0
lock = threading.Lock()


def increment():
    global counter

    for _ in range(100_000):
        with lock:
            counter += 1




# t1 = threading.Thread(target=increment)
# t2 = threading.Thread(target=increment)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# Lock
# → One thread at a time


# RLock
# → Same thread can acquire lock again


# Event
# → One thread signals another


# Semaphore
# → Limit number of concurrent workers


# threading.local()
# → Data belongs to one thread


def calculate():
    # very heavy calculation
    pass


# Process 1 → CPU Core 1
# Process 2 → CPU Core 2
# Process 3 → CPU Core 3
# Process 4 → CPU Core 4


from multiprocessing import Process


def work(name):
    print(f"Working: {name}")


p1 = Process(target=work, args=("Task 1",))
p2 = Process(target=work, args=("Task 2",))

p1.start()
p2.start()

p1.join()
p2.join()



from concurrent.futures import ThreadPoolExecutor


def download(file):
    print(f"Downloading {file}")
    return f"{file} done"


files = ["a.jpg", "b.jpg", "c.jpg", "d.jpg"]


with ThreadPoolExecutor(max_workers=4) as executor:
    results = executor.map(download, files)


for result in results:
    print(result)