# packing => test => build => publish(dist)  

# expense_tracker/
#     calculator.py
#     formatter.py
#     validator.py

# calcuator.zip

# from expense_tracker import calculator



# my-package/
# │
# ├── pyproject.toml => Project/package configuration
# ├── README.md # Documentation
# ├── LICENSE # Legal usage terms
# ├── CHANGELOG.md # Version history
# ├── .gitignore
# │
# ├── src/
# │   └── mypackage/ # Application/library source
# │       ├── __init__.py
# │       ├── calculator.py
# │       └── cli.py
# │
# ├── tests/ # Automated tests
# │   ├── test_calculator.py
# │   └── test_cli.py
# │
# └── .github/ # CI/CD
#     └── workflows/
#         └── ci.yml


# pyproject.toml

# setup.py
# setup.cfg
# requirements.txt
# MANIFEST.in


# flit
# setuptools
# pdm

# [build-system]
# requires = ["hatchling"]
# build-backend = "hatchling.build"

# [project]
# name = "decorator-toolkit"
# version = "1.0.0"
# description = "A collection of reusable Python decorators"
# readme = "README.md"
# requires-python = ">=3.11"
# license = { file = "LICENSE" }

# authors = [
#     { name = "Yogesh Yadav" }
# ]

# dependencies = []

# [project.urls]
# Homepage = "https://github.com/example/decorator-toolkit"
# Repository = "https://github.com/example/decorator-toolkit"
# Documentation = "https://github.com/example/decorator-toolkit#readme"



# npm run build 

# python -m build


# name
# version
# description
# readme
# authors
# license
# requires-python
# dependencies
# optional-dependencies
# scripts
# urls


# dependencies = [
#     "requests>=2.31,<3",
#     "pydantic>=2.0,<3"
# ]


# pip install requests

# pip install decorator-toolkit # npm install


# [project.optional-dependencies]

# dev = [
#     "pytest",
#     "ruff"
# ]

# test = [
#     "pytest",
#     "pytest-cov"
# ]

# docs = [
#     "mkdocs"
# ]

# pip install decorator-toolkit[dev]



# Production
#     ↓
# Application dependencies


# Development
#     ↓
# Production dependencies
# +
# Testing
# +
# Linting
# +
# Type checking



# src/decorator_toolkit/cli.py


# def main():
#     print("Decorator Toolkit")



# scripts

# [project.scripts]
# decorator-toolkit = "decorator_toolkit.cli:main"


# [project.urls]
# Homepage = "https://example.com"
# Documentation = "https://docs.example.com"
# Repository = "https://github.com/example/project"
# Changelog = "https://github.com/example/project/blob/main/CHANGELOG.md"


#"requests>=2.31,<3"


#pip install requests

# pip install --upgrade requests

# pip uninstall requests

# pip list

# pip install pip-audit



# project/
# │
# ├── pyproject.toml
# ├── README.md
# │
# ├── src/
# │   └── mypackage/
# │       ├── __init__.py
# │       ├── calculator.py
# │       └── cli.py
# │
# └── tests/


# # calculator.py

# def add(a, b):
#     return a + b


# from mypackage.calculator import add


# __all__ = [
#     "add",
#     "subtract",
# ]

# from importlib.metadata import versions

# print(versions("decorator-toolkit"))


# python -m pip install build

# python -m build

# dist/
# ├── decorator_toolkit-1.0.0-py3-none-any.whl # installation format.
# └── decorator_toolkit-1.0.0.tar.gz

# Instead of rebuilding everything from source every time, pip can install the wheel directly when compatible.


# pip install decorator_toolkit-1.0.0-py3-none-any.whl


# Changelog

# ## [1.1.0] - 2026-09-20

# ### Added
# - Added retry decorator.
# - Added CLI command.

# ### Changed
# - Improved logging.

# ### Fixed
# - Fixed timeout handling.

# ## [1.0.0] - 2026-09-10

# ### Added
# - Initial release.



# pypi