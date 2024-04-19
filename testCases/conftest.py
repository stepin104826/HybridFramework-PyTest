from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    return driver

def pytest_addoption(parser):          # This will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):            # This will return the browser value to the setup method
    return request.config.getoption("--browser")

#################### PyTest HTML Report #############################

# # Hook for adding environment info. to HTML Report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'nop Commerce'
#     config._metadata['Module Name'] = 'Customers'
#     config._metadata['Tester'] = 'Srikar'
#
# # Hook for deleting/modifying env. info. to HTML report
# @pytest.mark.parametrize
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)

