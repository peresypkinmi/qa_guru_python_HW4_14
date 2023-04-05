
import pytest
import time


@pytest.fixture()
def browser():
    """Какой-нибудь браузер - chrome or firefox"""
    time.sleep(1)


def test_first():
    time.sleep(1)


def test_second():
    time.sleep(1)
