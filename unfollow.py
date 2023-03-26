import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

# Ersetzen Sie diese Werte durch Ihre Instagram-Anmeldedaten
username = 'your_username'
password = 'your_password'

# Anmelden bei Instagram
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.instagram.com/')
time.sleep(2)

username_input = driver.find_element_by_name('username')
username_input.send_keys(username)
password_input = driver.find_element_by_name('password')
password_input.send_keys(password)
password_input.send_keys(Keys.ENTER)

time.sleep(4)

# Gehe zu Ihrem Profil
driver.get(f'https://www.instagram.com/{username}/')
time.sleep(2)

# Klicken Sie auf die Schaltfläche "Abonniert"
following_button = driver.find_element_by_xpath('//a[contains(@href, "/following/")]')
following_button.click()
time.sleep(2)

# Unfollow-Nutzer
unfollow_buttons = driver.find_elements_by_xpath('//button[text()="Abonniert"]')
for i, button in enumerate(unfollow_buttons):
    if i < 200: # Maximal 200 Nutzer
        button.click()
        time.sleep(2) # Warten Sie 2 Sekunden zwischen den Aktionen, um die Wahrscheinlichkeit einer Sperrung zu verringern

driver.quit()
