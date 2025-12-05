from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_expect_text_page_two():
    browser.element(
        (AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_forward_button")
    ).click()
    browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/primaryTextView")).should(
        have.exact_text("New ways to explore")
    )
