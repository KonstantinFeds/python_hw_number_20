
import os
from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options
import utils.file


def to_driver_options(context):
    options = UiAutomator2Options()

    if context == 'local_emulator':
        options.set_capability('remote_url', os.getenv('REMOTE_URL'))
        options.set_capability('deviceName', os.getenv('DEVICE_NAME'))
        options.set_capability('appWaitActivity', os.getenv('APP_WAIT_ACTIVITY'))
        options.set_capability('appActivity', 'org.wikipedia.main.MainActivity')
        options.set_capability('autoLaunch', True)
        options.set_capability('autoGrantPermissions', True)
        options.set_capability('app', utils.file.abs_path_from_project(os.getenv('APP')))
        options.set_capability('appPackage',os.getenv('APP_PACKAGE'))
        options.set_capability('platformName',os.getenv('PLATFORM_NAME'))

    if context == 'bstack':
        options.set_capability('remote_url', os.getenv('REMOTE_URL'))
        options.set_capability('deviceName', os.getenv('DEVICE_NAME'))
        options.set_capability('platformName', os.getenv('PLATFORM_NAME'))
        options.set_capability('platformVersion', os.getenv('PLATFORM_VERSION'))
        options.set_capability('appWaitActivity', os.getenv('APP_WAIT_ACTIVITY'))
        options.set_capability('app', os.getenv('APP'))
        load_dotenv(dotenv_path=utils.file.abs_path_from_project(
            '.env.credentials.credentials'))  # загрузка переменных окружения из файла .env.credentials.credentials
        options.set_capability(
            'bstack:options', {
                'projectName': 'Wikipedia project',
                'buildName': 'browserstack-build-1',
                'sessionName': 'BStack test',
                'userName': os.getenv('USER_NAME_BSTACK'),
                'accessKey': os.getenv('ACCESS_KEY_BSTACK'),
            },
        )

    return options


















"""
#код с урока

#context = os.getenv('context', 'bstack')
#run_on_bstack = os.getenv('run_on_bstack','false').lower() == 'true'
remote_url = os.getenv('remote_url','http://127.0.0.1:4723')
deviceName = os.getenv('deviceName')
appActivity = os.getenv('appActivity','org.wikipedia.main.MainActivity')
app = os.getenv('app','./app-alpha-universal-release.apk')
runs_on_bstack = app.startswith('bs://')
appPackage = os.getenv('appPackage','org.wikipedia.alpha')
if runs_on_bstack:
    remote_url = 'http://hub.browserstack.com/wd/hub'
USER_NAME_BSTACK = os.getenv('bstack_userName', 'bsuser_SVwepu')
ACCESS_KEY_BSTACK = os.getenv('bstack_accessKey', 'RbgXQs1ipEuaWioynt6U')

"""