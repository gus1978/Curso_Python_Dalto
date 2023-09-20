from concurrent.futures import thread
from typing import KeysView
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = "https://google.com"
path = "C:\Drivers/chromedriver.exe"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

driver.find_element(by= "name", value="q")
driver.send_keys("automatización")
driver.send_keys(KeysView.RETURN)

thread.sleep(1500)
