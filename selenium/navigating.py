from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

PATH = "/home/joaogui/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Python Programming"))
    )
    element.clear()
    element.click()

    driver.back()
except:
    quit()