import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Manual Way
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://seleniumbase.io/demo_page");
#
# driver.find_element(By.XPATH,"/html/body/form/table/tbody/tr[7]/td[3]/label").click()

# --------------------------------------------------------------------------


element = driver.find_element(By.ID, 'mySelect')
dropdown = Select(element)                                            #import Select (Webdriver)
# Select will generate the object by taking the element input
# To check the what select does, go on it and right click on it--> Go to -->Implementations

# time.sleep(3)                       #3 second wait
# dropdown.select_by_index(0)
# Selects the 3rd index from dropdown
# 0th index is 25%, 1st index is 50%, 3rd index is 75%, 4th index is 100%

# time.sleep(3)
# dropdown.select_by_value('50%')
#
# time.sleep(3)
# dropdown.select_by_visible_text('Set to 75%')
#

options = dropdown.options
# property - No input, Gives o/p
print(options)

# Task :I want to print the options visible text and values.
#  loop and print 2 lines









# Difference between find element and find elements
# find element- Single element as o/p
# find elements - Multiple elements as O/P, if same name it will give 1st o/p


# Difference between XPATH and Full XPATH
# Full XPATH- Gives total address as per hararchie
# XPATH - Gives the optimized path, directly analyse ID