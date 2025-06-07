import time
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@given('the user is on the Register page')
def register_page(context):
    context.driver.find_element(By.ID, "signin2").click()
    WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.ID, "signInModal"))
    )


@given('the user enter {username} as username')
def user_name(context, username):
    time.sleep(1)
    input_field = context.driver.find_element(By.ID, "sign-username")
    input_field.clear()
    input_field.send_keys(username)
    entered = input_field.get_attribute("value")
    assert entered == username, f"Expected username '{username}', got '{entered}'"


@given('the user enter {password} as password')
def pass_word(context, password):
    input_field = context.driver.find_element(By.ID, "sign-password")
    input_field.clear()
    input_field.send_keys(password)
    entered = input_field.get_attribute("value")
    assert entered == password, f"Expected password '{password}', got '{entered}'"


@when('the user click on SignUp button')
def sign_up(context):
    context.driver.find_element(By.XPATH, '//button[@onclick="register()"]').click()
    WebDriverWait(context.driver, 5).until(EC.alert_is_present())
    alert = context.driver.switch_to.alert
    print("Alert text:", alert.text)
    assert "Sign up successful" in alert.text or "This user already exist" in alert.text
    alert.accept()


@then('registration should be displayed successfully')
def regi_station(context):
    print("Registration attempt completed.")
    context.driver.find_element(By.XPATH,"//div[@id='signInModal']//span[@aria-hidden='true'][normalize-space()='×']").click()
    time.sleep(5)
