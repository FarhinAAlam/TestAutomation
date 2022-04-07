import pytest
import pyTestDemo.Calculator as Cal
  # as caldewate  r pyTestDemo.Calculator.add likha lagbe na er bodole cal.add

@pytest.mark.smokeAddTest

def test_add():
    assert Cal.add(10, 5) == 15


    def test_sub():

        assert Cal.sub(20, 10) == 10

