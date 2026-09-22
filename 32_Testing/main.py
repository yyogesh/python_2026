from sys import exc_info


def add_expense(amount, tax):
    return amount + tax


def test_add_expense():
    assert add_expense(100, 10) == 110


if __name__ == "__main__":
    test_add_expense()



# python -m pytest


# project/
# │
# ├── src/
# │   └── expense_tracker/
# │       └── calculator.py
# │
# └── tests/
#     └── test_calculator.py

# test_*.py
# *_test.py


def test_user():
    user = {
        "name": "Yogesh",
        "age": 37
    }

    assert user["name"] == "Yogesh"
    assert user["age"] == 37


# pytest



def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient balance")

    return balance - amount



def test_withdraw_insufficient_balance():
    with pytest.raises(ValueError):
        withdraw(100, 200)

    assert str(exc_info.value) == "Insufficient balance"



assert 0.1 + 0.2 == 0.3

def test_total():
    result = 0.1 + 0.2

    assert result == pytest.approx(0.3)


assert result == pytest.approx(
    0.3,
    abs=0.001
)



import warnings

def old_function():
    warnings.warn(
        "This function is deprecated",
        DeprecationWarning
    )


def test_old_function_warning():
    with pytest.warns(DeprecationWarning):
        old_function()


def test_warning_message():
    with pytest.warns(DeprecationWarning) as record:
        old_function()

    assert "deprecated" in str(record[0].message)

# xit test.skip

@pytest.mark.skip(reason="Feature not implemented")
def test_future_feature():
    assert True


@pytest.mark.skipif(
    True,
    reason="Requires Windows"
)
def test_windows_feature():
    ...


@pytest.mark.xfail(reason="Known bug")
def test_known_bug():
    assert 10 == 20



def test_user_name():
    user = {
        "name": "Yogesh",
        "role": "admin"
    }

    ...


def test_user_role():
    user = {
        "name": "Yogesh",
        "role": "admin"
    }



@pytest.fixture
def user():
    return {
        "name": "Yogesh",
        "role": "admin"
    }


def test_user_name(user):
    assert user["name"] == "Yogesh"


def test_user_role(user):
    assert user["role"] == "admin"



@pytest.fixture
def database():
    db = create_database()

    yield db

    db.close()



# conftest.py # Shared testing infrastructure for a directory.

# @pytest.fixture
# def user():
#     return {
#         "id": 1,
#         "name": "Yogesh"
#     }

# tests/
# │
# ├── conftest.py
# ├── test_users.py
# ├── test_expenses.py
# └── test_reports.py


def test_file(tmp_path):
    file = tmp_path / "data.txt"

    file.write_text("Hello")

    assert file.read_text() == "Hello"



def test_print(capsys):
    print("Hello")

    captured = capsys.readouterr()

    assert captured.out == "Hello\n"



def test_logging(caplog):
    import logging

    logging.warning("Something happened")

    assert "Something happened" in caplog.text



def get_environment():
    import os
    return os.getenv("APP_ENV")



def test_get_environment(monkeypatch):
    monkeypatch.setenv("APP_ENV", "test")

    assert get_environment() == "test"



def register_user(user, email_service):
    save_user(user)
    email_service.send_welcome_email(user["email"])


from unittest.mock import Mock

def test_register_user():
    user = {
        "name": "Yogesh",
        "email": "yogesh@me.com"
    }

    email_service = Mock()

    register_user(user, email_service)

    email_service.send_welcome_email.assert_called_with(user["email"])


#     mock.send.assert_called_once_with(
#     "hello"
# )


#  pytest-cov



# expense_tracker/
# │
# ├── src/
# │   └── expense_tracker/
# │       ├── calculator.py
# │       ├── service.py
# │       └── repository.py
# │
# ├── tests/
# │   ├── conftest.py
# │   ├── test_calculator.py
# │   ├── test_service.py
# │   └── test_repository.py
# │
# └── pytest.ini

# setup.py
# setup.cfg
# requirements.txt
# MANIFEST.in


# my-package/
# │
# ├── pyproject.toml
# ├── README.md
# ├── LICENSE
# ├── CHANGELOG.md
# ├── .gitignore
# │
# ├── src/
# │   └── mypackage/
# │       ├── __init__.py
# │       ├── calculator.py
# │       └── cli.py
# │
# ├── tests/
# │   ├── test_calculator.py
# │   └── test_cli.py
# │
# └── .github/
#     └── workflows/
#         └── ci.yml





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