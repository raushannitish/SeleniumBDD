import time

from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


@when('the user click on product name')
def product_name(context):
    time.sleep(10)
    context.driver.find_element(By.CSS_SELECTOR,".hrefch[href^='prod.html?idp_=3']").click()
    context.driver.find_element(By.XPATH,"//div[@class='row']//a[.='Add to cart']").click()


@then('that product be successfully added')
def sucess_added(context):
    wait=WebDriverWait(context.driver,10).until(EC.alert_is_present())
    alert=context.driver.switch_to.alert
    alert.accept()


@when('the user click on cart button')
def cart_button(context):
    context.driver.find_element(By.ID,'cartur').click()

@then('the selected product should be visible')
def product_visible(context):
    val=WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME,'success')))
    assert val.is_displayed(),"Please check the product"

@then('the user click on placeOrder button')
def place_order(context):
    context.driver.find_element(By.XPATH,"//button[normalize-space()='Place Order']").click()

@then('the user able to put all the details')
def all_details(context):
    context.driver.find_element(By.XPATH,"//div[@class='modal-body']//input[@id='name']").send_keys("Deepak")
    context.driver.find_element(By.XPATH, "//div[@class='modal-body']//input[@id='country']").send_keys("India")
    context.driver.find_element(By.XPATH, "//div[@class='modal-body']//input[@id='city']").send_keys("Bihar")
    context.driver.find_element(By.XPATH, "//div[@class='modal-body']//input[@id='card']").send_keys("123456789")
    context.driver.find_element(By.XPATH, "//div[@class='modal-body']//input[@id='month']").send_keys("July")
    context.driver.find_element(By.XPATH, "//div[@class='modal-body']//input[@id='year']").send_keys("2025")
    context.driver.find_element(By.XPATH, "//button[normalize-space()='Purchase']").click()
    confirm_text = WebDriverWait(context.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Thank you')]")))
    assert "Thank you" in confirm_text.text
    context.driver.find_element(By.XPATH, "//button[text()='OK']").click()
    context.driver.find_element(By.XPATH,"//div[@id='orderModal']//span[@aria-hidden='true'][normalize-space()='×']").click()










