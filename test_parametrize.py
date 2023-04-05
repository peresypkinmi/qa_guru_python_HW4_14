from dataclasses import dataclass

import pytest


def test_with_param(browser):
    pass


def test_with_matrix_param(browser, test_user):
    pass


def test_with_param_marks(browser):
    pass

# ---------------------------------------------


def browser(request):
    pass


def test_with_parametrized_fixture(browser):
    pass


def test_with_indirect_parametrization(browser):
    pass


# @common_user
def test_with_account(test_user):
    pass


@dataclass
class User:
    id: int
    name: str
    age: int
    description: str

    def __repr__(self):
        return f"{self.name} ({self.id})"


user1 = User(id=1, name="Mario", age=32, description="something " * 10)
user2 = User(id=2, name="Wario", age=62, description="else " * 10)


@pytest.mark.parametrize("user", [user1, user2])
def test_users(user):
    print()
