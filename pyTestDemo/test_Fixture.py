import pytest
@pytest.fixture()

def browser_launch():
    print(" Browser launched successfully")
    return

def open_loginurl(browser_launch):
    print(" Login page  open Successfully ")
def login_test_001(browser_launch):

    print(" Login Test passed ")
def  browser_close(browser_launch):
    print(" Browser close successfully")