from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/");
 # Write click on the part to be inspected to find out the id of the same
# Go to inspect and go to select the element through the mouse at top left corner

#To find the id, web element and save into variable
# inputEmail = driver.find_element_by_id("email")
inputEmail = driver.find_element(By.ID,"email")
inputEmail.send_keys("harshalshinde9168921075@gmail.com")

# inputPass = driver.find_element_by_id("pass")
inputPass = driver.find_element(By.ID,"pass")
inputPass.send_keys("Harsh@123")

# inputButton = driver.find_element_by_id("u_0_5_+5")
# inputButton.click();
# selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"css selector","selector":"[id="loginbutton"]"}
#   (Session info: chrome=103.0.5060.66)

# Facebook is changing the id of the login button everytime (it is dynamic)
# So we can't depend on the id

# inputButton = driver.find_element_by_name("login")
# inputButton = driver.find_element(By.NAME, "login")
# inputButton.click();

# //*[@id="loginbutton"]

inputButton = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/form/div/div[3]/button")
inputButton.click()
# DeprecationWarning
# No error its just warning, says for latest version use
# Require 2 elements # to use By function have to "import By"

# find_element(by=By.NAME, value=name)
#   inputButton = driver.find_element_by_name("login")

# After using find_element there is no error

# Element finding methods
# 1. find_element_by_id
# 2. find_element_by_name
# 3. XPATH / Full XPATH --Dynamic
#