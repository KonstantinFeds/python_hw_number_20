from appium.webdriver.common.appiumby import AppiumBy
from selene import browser,have


def test_expect_text_page_four():
    browser.element((AppiumBy.ANDROID_UIAUTOMATOR,'className("android.widget.LinearLayout").instance(9)')).click()
    browser.element((AppiumBy.ID,'org.wikipedia.alpha:id/primaryTextView')).should(have.exact_text('Data & Privacy'))