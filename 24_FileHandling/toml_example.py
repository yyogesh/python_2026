# [database]
# host = "localhost"
# port = 5432
# username = "admin"

# [application]
# debug = true

import tomllib

# tomli-w is a TOML parser for Python

with open("config.toml", "rb") as f:
    config = tomllib.load(f)

print(config["database"]["host"])
print(config["application"]["debug"])



text = """
[server]
host = "localhost"
port = 8000
"""

config = tomllib.loads(text)
print(config["server"]["host"])


import configparser


config = configparser.ConfigParser()
config.read("config.ini")

print(config["server"]["host"])