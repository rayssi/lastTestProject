import time

from behave import *
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from config import driver

url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"


@given(u'user at login page')
def step_impl(context):
    driver.get(url)


@when(u'user insert correct emil and password')
def step_impl(context):
    print("test")
    EmailInput = driver.find_element(By.NAME, "username")
    EmailInput.send_keys("admin")

    PasswordInput = driver.find_element(By.NAME, "password")
    PasswordInput.send_keys("admin123")
    print("close")

@when(u'user Click login button')
def step_impl(context):
    driver.find_element(By.XPATH,
                        "//body/div[@id='app']/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/form[1]/div[3]/button[1]").click()


@then(u'use should be in home page')
def step_impl(context):
    print("close")
    try:
        # identify element
        l = driver.find_element(By.TAG_NAME, "h6")
        s = l.text
        print("Element exist -" + s)
        print("Element exist")
        time.sleep(40)
    # NoSuchElementException thrown if not present
    except NoSuchElementException:
        print("Element does not exist")
        print("close")
        driver.close()
    #


# driver.close()
