import pytest
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome browser")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("Launching Firefox browser")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


# PyTest HTML Report

# It is a hook for adding environment info to HTML Report
def pytest_configure(config):
    config._metadata["Project Name"] = "nop Commerce"
    config._metadata["Module Name"] = "Customers"
    config._metadata["Tester"] = "Kruse"


# It is a hook for delete/modify environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

