import pyTestDemo.Calculator as Cal
import pytest

@pytest.mark.smokeAddTest

def test_add():
    assert Cal.add(10, 5) == 15


def test_multiply():
    assert  Cal.multiply(4, 3)  == 12

    def  test_division():
        assert Cal.division(50, 25) == 2