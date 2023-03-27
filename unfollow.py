import time
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


 
options = Options()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


# Replace these values with your Instagram credentials
username = 'xxxxxxxx'
password = 'xxxxxxxx'


# Login to Instagram
driver.get('https://www.instagram.com/')
time.sleep(5)
# skip cookies
confirm_cookies_xpath = '//button[contains(@class, "_a9--") and contains(@class, "_a9_1")]'
confirm_cookies = driver.find_element(By.XPATH, confirm_cookies_xpath)
confirm_cookies.click()
time.sleep(5)

username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
username_input.send_keys(username)
password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
password_input.send_keys(password)
password_input.send_keys(Keys.ENTER)

time.sleep(10)  # # Wait after login before navigating to the next page

# Go to your profile
driver.get(f'https://www.instagram.com/{username}/')
time.sleep(5)

# Click the Subscribed button
following_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "/following/")]')))
following_button.click()
time.sleep(10) 

# Unfollow-User
unfollow_buttons_xpath = '//button[contains(@class, "_acan") and contains(@class, "_acap") and contains(@class, "_acat") and contains(@class, "_aj1-")]'
confirm_unfollow_xpath = '//button[contains(@class, "_a9--") and contains(@class, "_a9-_")]'

for i in range(15):  # Maximal 25 User at one time or you can be blocked!
    try:
        unfollow_button = driver.find_element(By.XPATH, unfollow_buttons_xpath)
        unfollow_button.click()
        time.sleep(3 + 9 * random.random())  # Wait between 3-12 seconds between actions to reduce chances of getting banned

        # Check that the confirmation dialog appears and click the confirmation button
        try:
            confirm_unfollow_button = driver.find_element(By.XPATH, confirm_unfollow_xpath)
            confirm_unfollow_button.click()
            time.sleep(3)
        except NoSuchElementException:
            pass  # confirmation dialog was not shown; go on

    except NoSuchElementException:
        break  # No more unfollow buttons were found; end the loop


driver.quit()
