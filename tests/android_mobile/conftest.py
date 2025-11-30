import os
import allure
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from requests import options
from selene import browser
#from tests.android_mobile.mobile.android.utils.allure import attach_bstack_video_android
from utils.allure import attach_bstack_video_android
import config
import utils.file

import pytest
from appium import webdriver
from dotenv import load_dotenv
from selene import browser
import config
#from utils import at


def pytest_addoption(parser):
    parser.addoption(
        "--context",
        default="bstack",
        help="Specify the test context"
    )


def pytest_configure(config):
    context = config.getoption("--context")
    env_file_path = f".env.{context}"

    load_dotenv(dotenv_path=env_file_path)


@pytest.fixture
def context(request):
    return request.config.getoption("--context")


@pytest.fixture(scope='function', autouse=True)
def mobile_management(context):


    options = config.to_driver_options(context=context)

    browser.config.driver = webdriver.Remote(options.get_capability('remote_url'), options=options)
    browser.config.timeout = 10.0

    yield

    #attach.add_screenshot()
    #attach.add_xml()
    #session_id = browser.driver.session_id

    browser.quit()

    # if context == 'bstack':
    #     attach.add_video(session_id)




"""
#код с урока

@pytest.fixture(scope="function", autouse=True)
def mobile_management():

    options = UiAutomator2Options()

    if config.deviceName:
        options.set_capability('deviceName', config.deviceName)

    if config.appActivity:
        options.set_capability('appActivity', config.appActivity)

    if config.appPackage:
        options.set_capability('appPackage', config.appPackage)

    options.set_capability('app',(
        config.app if (config.app.startswith('/') or config.runs_on_bstack)
        else utils.file.abs_path_from_project(config.app)
    ))

    if config.runs_on_bstack:
        options.set_capability(
            "bstack:options", {
                "projectName": "First Python project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test",
                # Set your access credentials
                "userName": config.USER_NAME_BSTACK,
                "accessKey": config.ACCESS_KEY_BSTACK
                # "userName": USER_NAME_BSTACK,
                # "accessKey": ACCESS_KEY_BSTACK,
            },

        )

    browser.config.driver = webdriver.Remote(
        config.remote_url,
        options=options)

    yield

"""
