import pytest
import pyTestDemo.Calculator as Cal
  # as caldewate  r pyTestDemo.Calculator.add likha lagbe na er bodole cal.add

def test_add():
    assert Cal.add(10, 5) == 15

@pytest.mark.skip(reason = " No need this iteration") # kono ekta funtion skip korte chaile tar aghe  eta likhbo
def test_multiply():
    assert  Cal.multiply(4, 3)  == 12

    def  test_division():
        assert Cal.division(50, 25) == 2

