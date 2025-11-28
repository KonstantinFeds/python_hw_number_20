import os
import allure
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from dotenv import load_dotenv
from selene import browser
#from tests.android_mobile.mobile.android.utils.allure import attach_bstack_video_android


@pytest.fixture(scope="function", autouse=True)
def mobile_management():

    #load_dotenv()


    URL ='http://127.0.0.1:4723'

    with allure.step("Настройка конфигураций под android для BrowserStack "):

        options = UiAutomator2Options().load_capabilities(
            {
                # Specify device and os_version for testing
                "platformName": "android",
                #"platformVersion": "12.0",
                "deviceName": "emulator-5554",
                # Set URL of the application under test
                "app": "C:/Users/kfedoseev/Downloads/app-alpha-universal-release.apk",
                "appActivity":"org.wikipedia.main.MainActivity",
                "appPackage":"org.wikipedia.alpha"
                # Set other BrowserStack capabilities

            }
        )

    browser.config.driver = webdriver.Remote(URL, options=options)

    yield

    # session_id = browser.driver.session_id
    #
    # with allure.step("Закрытие сессии"):
    #     browser.quit()
    #
    # attach_bstack_video_android(session_id)