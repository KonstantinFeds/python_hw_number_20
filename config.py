import os
from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options
import utils.file


def to_driver_options(context):
    options = UiAutomator2Options()

    if context == "local_emulator":
        options.set_capability("remote_url", os.getenv("REMOTE_URL"))
        options.set_capability("deviceName", os.getenv("DEVICE_NAME"))
        options.set_capability("appWaitActivity", os.getenv("APP_WAIT_ACTIVITY"))
        options.set_capability(
            "app", utils.file.abs_path_from_project(os.getenv("APP"))
        )

    if context == "bstack":
        options.set_capability("remote_url", os.getenv("REMOTE_URL"))
        options.set_capability("deviceName", os.getenv("DEVICE_NAME"))
        options.set_capability("platformName", os.getenv("PLATFORM_NAME"))
        options.set_capability("platformVersion", os.getenv("PLATFORM_VERSION"))
        options.set_capability("appWaitActivity", os.getenv("APP_WAIT_ACTIVITY"))
        options.set_capability("app", os.getenv("APP"))
        load_dotenv(
            dotenv_path=utils.file.abs_path_from_project(".env.credentials")
        )  # загрузка переменных окружения из файла .env.credentials
        options.set_capability(
            "bstack:options",
            {
                "projectName": "First Python project",
                "buildName": "browserstack-task-number-20",
                "sessionName": "BStack android test",
                "userName": os.getenv("USER_NAME_BSTACK"),
                "accessKey": os.getenv("ACCESS_KEY_BSTACK"),
            },
        )

    return options
