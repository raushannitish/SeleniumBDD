import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@given('user open the login page')
def log_in(context):
    context.driver.find_element(By.ID,"login2").click()
    time.sleep(5)

@given('the user enter "{usename}" as usename')
def use_name(context,usename):
    input_field=context.driver.find_element(By.ID,"loginusername")
    input_field.clear()
    input_field.send_keys(usename)
    expected_output=input_field.get_attribute("value")
    assert expected_output==usename,"Please Check"

@given('the user enter "{pasword}" as pasword')
def use_pass(context,pasword):
    input_field=context.driver.find_element(By.ID,"loginpassword")
    input_field.clear()
    input_field.send_keys(pasword)
    expected_output=input_field.get_attribute("value")
    assert expected_output==pasword,"Please Check"

@when('the user click on login button')
def lo(context):
    context.driver.find_element(By.XPATH, '//button[@onclick="logIn()"]').click()



@then('login should be happen')
def bu_tton(context):
    time.sleep(5)
    message=context.driver.find_element(By.ID,"nameofuser").text
    assert message.startswith("Welcome "), "Expected prefix 'Welcome ' missing"

@then('the user sucessfully logout')
def log_out(context):
    context.driver.find_element(By.ID,"logout2").click()
    wc=WebDriverWait(context.driver,10).until(EC.visibility_of_element_located((By.ID,"signin2")))
    assert wc.is_displayed(),"Please check the following details"

@then('error alert should be shown')
def er(context):
    WebDriverWait(context.driver, 3).until(EC.alert_is_present())
    alert = context.driver.switch_to.alert
    print(alert.text)
    alert.accept()
    close_button = context.driver.find_element(By.XPATH, "//div[@id='logInModal']//button[@class='close']")
    close_button.click()





