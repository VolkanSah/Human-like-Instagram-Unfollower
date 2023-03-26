import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--lang=de')  # Füge diese Zeile hinzu, um die Sprache auf Deutsch zu setzen
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Ersetzen Sie diese Werte durch Ihre Instagram-Anmeldedaten
username = 'anna_krukover'
password = '@BH@2309'

# Anmelden bei Instagram
driver.get('https://www.instagram.com/')
time.sleep(5)

username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'username')))
username_input.send_keys(username)
password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
password_input.send_keys(password)
password_input.send_keys(Keys.ENTER)

# Gehe zu Ihrem Profil
driver.get(f'https://www.instagram.com/{username}/following/')
time.sleep(5)
print(driver.page_source)


# Unfollow-Nutzer
unfollow_buttons_xpath = 'unfollow_buttons_xpath = '//button[contains(text(), "Gefolgt")]'
confirm_unfollow_xpath = 'unfollow_buttons_xpath = '//button[contains(text(), "Nicht mehr folgen")]'

for i in range(25): # Maximal 25 Nutzer
    try:
        unfollow_button = driver.find_element_by_xpath(unfollow_buttons_xpath)
        unfollow_button.click()
        time.sleep(2) # Warten Sie 2 Sekunden zwischen den Aktionen, um die Wahrscheinlichkeit einer Sperrung zu verringern
      
# Prüfen, ob der Bestätigungsdialog angezeigt wird, und klicken Sie auf die Bestätigungsschaltfläche
try:
    confirm_unfollow_button = driver.find_element_by_xpath(confirm_unfollow_xpath)
    print("Bestätigungsdialog gefunden.") # Debug-Ausgabe
    confirm_unfollow_button.click()
    time.sleep(3)
except NoSuchElementException:
    print("Bestätigungsdialog wurde nicht angezeigt.") # Debug-Ausgabe
    pass # Bestätigungsdialog wurde nicht angezeigt; fahren Sie fort

print(driver.page_source)

driver.quit()
