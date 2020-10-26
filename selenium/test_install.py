from selenium import webdriver
PATH = "/home/joaogui/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://joaogui1.netlify.app")
print(driver.title)
driver.quit()