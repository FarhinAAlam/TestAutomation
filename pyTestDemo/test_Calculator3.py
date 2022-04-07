import pyTestDemo.Calculator as Cal
import pytest

@pytest.mark.smokeAddTest

  # as caldewate  r pyTestDemo.Calculator.add likha lagbe na er bodole cal.add
def test_add():
    assert Cal.add(10, 5) == 15

    def test_multiply():
        assert Cal.multiply(4, 3) == 12

