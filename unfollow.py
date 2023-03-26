import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
 
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


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
time.sleep(10)

# Unfollow-Nutzer
# unfollow_buttons = driver.find_elements_by_xpath('//button[text()="Abonniert"]')
unfollow_button = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/div/div/div[3]/div')
for i, button in enumerate(unfollow_buttons):
    if i < 200: # Maximal 200 Nutzer
        button.click()
        time.sleep(2) # Warten Sie 2 Sekunden zwischen den Aktionen, um die Wahrscheinlichkeit einer Sperrung zu verringern

driver.quit()
