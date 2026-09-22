# functools is a standard library module that provides higher-order functions for functional programming. 
# It includes tools for working with iterators, function decorators, and more.

# lru_cache is a decorator that caches the results of a function based on its arguments. 
# It is useful for reducing the number of function calls when the same arguments are passed multiple times.

from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# operator is a standard library module that provides functions for performing common operations on objects, such as arithmetic, comparison, and logical operations.
# It can be used to create more readable and efficient code by replacing lambda functions with built-in operator functions.

from operator import add, sub, mul, truediv

# itemtools is a standard library module that provides functions for creating and working with iterators.
# It includes functions for creating iterators from iterables, such as map, filter, and zip.

# collections is a standard library module that provides alternatives to built-in data types, such as namedtuples, defaultdicts, and ordered dictionaries.



# | Module               | Purpose                                |
# | -------------------- | -------------------------------------- |
# | `os`                 | Operating system interaction           |
# | `sys`                | Python runtime and interpreter info    |
# | `logging`            | Structured logging                     |
# | `argparse`           | Command-line interfaces                |
# | `csv`                | CSV reading and writing                |
# | `sqlite3`            | Built-in SQL database                  |
# | `hashlib`            | Hashing (SHA-256, MD5, etc.)           |
# | `secrets`            | Cryptographically secure random values |
# | `urllib.parse`       | URL parsing and encoding               |
# | `concurrent.futures` | Thread and process pools               |
# | `multiprocessing`    | Process-based parallelism              |
# | `threading`          | Thread-based parallelism               |
# | `asyncio`            | Asynchronous I/O and concurrency       |
# | `socket`             | Low-level networking                   |