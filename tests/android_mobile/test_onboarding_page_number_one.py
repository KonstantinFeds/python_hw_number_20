import pytest
import allure
from selene import browser,have
from appium.webdriver.common.appiumby import AppiumBy



def test_add_language():

    browser.element((AppiumBy.ID,"org.wikipedia.alpha:id/addLanguageButton")).click()
    browser.element((AppiumBy.ANDROID_UIAUTOMATOR,'text("Add language")')).click()
    browser.element((AppiumBy.ANDROID_UIAUTOMATOR,'className("android.widget.Button").instance(1)')).click()
    browser.element((AppiumBy.ANDROID_UIAUTOMATOR, 'text("Search for a language")')).click()
    browser.element((AppiumBy.CLASS_NAME, "android.widget.EditText")).type("Russian")
    browser.element((AppiumBy.ANDROID_UIAUTOMATOR,'text("Русский")')).click()
    browser.element((AppiumBy.ACCESSIBILITY_ID,'Navigate up')).click()
    browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/option_label"))[1].should(have.text("Русский"))
