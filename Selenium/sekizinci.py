from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path="/Users/Melih/Desktop/chromedriver")
base_url = "https://clarusway.com/"
driver.get(base_url)
element = driver.find_element_by_id("EMBED_FORM_EMAIL_LABEL")
element.send_keys("merhaba")
time.sleep(5)
element.clear()
time.sleep(3)
driver.quit()