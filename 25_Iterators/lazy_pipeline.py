# 2026-09-07 10:00:01 INFO User logged in
# 2026-09-07 10:01:12 ERROR Database timeout
# 2026-09-07 10:02:10 INFO Request completed


def read_logs(filename):
    with open(filename) as file:
        for line in file:
            yield line

def error_logs(lines):
    for line in lines:
        if "ERROR" in line:
            yield line

def parse_logs(lines):
    for line in lines:
        parts = line.strip().split()

        yield {
            "date": parts[0],
            "time": parts[1],
            "level": parts[2],
            "message": " ".join(parts[3:])
        }

logs = read_logs("application.log")

errors = error_logs(logs)

parsed = parse_logs(errors)

for log in parsed:
    print(log)



def numbers():
    for number in range(1_000_000):
        yield number


def squares(values):
    for value in values:
        yield value * value


def even(values):
    for value in values:
        if value % 2 == 0:
            yield value