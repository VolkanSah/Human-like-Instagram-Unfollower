# you can test your configuration of your system with this test.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("https://www.google.com")

search_box = driver.find_element_by_css_selector("input[name='q']")
print("Suchfeld gefunden:", search_box)

driver.quit()

