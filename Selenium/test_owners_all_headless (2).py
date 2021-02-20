from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import os

driver = webdriver.Chrome(executable_path="/Users/Melih/Desktop/chromedriver")

# Connect to the application
APP_IP = os.environ['MASTER_PUBLIC_IP']  # master_public_ip icin terminalde export MASTER_PUBLIC-IP=3.238.205.252 yaz
url = "http://"+APP_IP.strip()+":8080/"

driver.get(url)

sleep(5)

owners_link = driver.find_element_by_link_text("OWNERS")
owners_link.click()
sleep(2)

all_link = driver.find_element_by_link_text("ALL")
all_link.click()
sleep(2)

# Verify that table loaded
sleep(1)
verify_table = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "table")))

print("Table loaded")

driver.quit()