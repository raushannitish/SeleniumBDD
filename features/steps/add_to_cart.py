from selenium import webdriver
from behave import *
from selenium.webdriver.common.by import By


@when('the user click on product name')
def product_name(context):
    context.driver.find_element(By.CSS_SELECTOR,".hrefch[href^='prod.html?idp_=3']").click()
    context.driver.find_element(By.XPATH,"//div[@class='row']//a[.='Add to cart']").click()
    alert=context.driver.switch_to.alert

@then()