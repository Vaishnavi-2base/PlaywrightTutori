import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.w3schools.com/")
driver.implicitly_wait(3)
driver.find_element(By.XPATH,"//a[@title='Sign Up to Improve Your Learning Experience']").click()

emailID = "tefd@bcd.com"
windowsOpened= driver.window_handles
driver.switch_to.window(windowsOpened[0])

Email_input = driver.find_element(By.XPATH, "//input[@placeholder='email']").send_keys(emailID)

password_input = driver.find_element(By.XPATH,"//input[@placeholder='password']").send_keys("Agsi0714@")

firstName = driver.find_element(By.XPATH,"//input[@placeholder='first name']").send_keys("Asjin")

LastName = driver.find_element(By.XPATH,"//input[@placeholder='last name']").send_keys("johfn")
CheckBox= driver.find_element(By.XPATH,"//input[@type='checkbox']")

if not CheckBox.is_selected():
    CheckBox.click()


SignUp_Button= driver.find_element(By.XPATH,"//button[text()='Sign Up']").click()

success_message= driver.find_element(By.CLASS_NAME,"Alert_iwrp__QeFaP ").text
print(success_message)

if emailID in success_message:
    print("email id is match")
else:
    print("email id is not match")


driver.find_element(By.XPATH,"//button[text()=' Return to login ']").click()


time.sleep(2)