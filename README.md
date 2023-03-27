## Requirements
Python 3
Python3-pip
Selenium
Webdriver Manager
### Install the required Python packages with the following command:
    sudo apt-get update
    sudo apt-get install -y libxss1 libappindicator1 libindicator7
    pip install -U selenium webdriver_manager

    
## Usage
Replace the username and password variables in the script with your Instagram account credentials.
Adjust the number of scroll operations in the script depending on the number of followers you want to load.
Run the script with the following command:

      python unfollow.py


error


Traceback (most recent call last):
  File "/home/comin/Schreibtisch/Script/unfollow.py", line 53, in <module>
    unfollow_button = driver.find_element_by_css_selector(unfollow_buttons_css)
AttributeError: 'WebDriver' object has no attribute 'find_element_by_css_selector'
