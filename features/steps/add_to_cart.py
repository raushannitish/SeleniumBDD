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




