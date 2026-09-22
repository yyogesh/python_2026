from contextlib import contextmanager, suppress, surpress
import time

@contextmanager
def database():
    print("Connecting")

    connection = "DB Connection"

    yield connection

    print("Closing")


with database() as db:
    print("Using:", db)



@contextmanager
def open_file(path, mode):
    f = open(path, mode)
    try:
        yield f          # this value is what "as f" receives
    finally:
        f.close()        # guaranteed to run, even if an error occurs

with open_file("test.txt", "w") as f:
    f.write("Hello")



# with suppress(FileNotFoundError):
#     open("missing.txt")



# class AsyncDatabase:
#     async def __aenter__(self):
#         print("Async connect")
#         return self

#     async def __aexit__(self, exc_type, exc_value, traceback):
#         print("Async close")


# async def main():
#     async with AsyncDatabase() as db:
#         print("Using:", db)



class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.elapsed = time.perf_counter() - self.start
        print(f"Elapsed: {self.elapsed:.4f} seconds")


with Timer():
    total = sum(range(1_000_000))