# Best Human Like - Instagram Unfollower (2023)

The Best Human Like - Instagram Unfollower (2023) is a powerful tool designed to detect and remove suspicious followers on your Instagram account. Originally created as a private GitHub repository for use with the [Instagram Suspicious Followers Detection](https://github.com/VolkanSah/Instagram-Suspicious-Followers-Detection) script, this tool is now available for public use.

Please note that this tool is intended for ethical use only and should not be used for harmful purposes. We do not provide an import feature for suspicious_followers.txt to prevent abuse by script kiddies. If you use this tool ethically, you know how to import the data.

**I appreciate your support and would be grateful if you could share this project with others and give us a "star" on GitHub or become a sponsor.**


⚠️ **Warning**: This script automates the process of unfollowing users on Instagram. Use it at your own risk. The author takes no responsibility for any consequences resulting from the use of this script. The copyright of this script remains with the author. ⚠️
### Setup for Debian/Ubuntu. unfollow.py can work on other systems , too.

This script is set up to look like a human, using random time intervals between actions to avoid detection. It's best to run it using a cron job. 
- Important resources for me: https://selenium-python.readthedocs.io/locating-elements.html

## Prerequisites

- Python 3
- pip
- Google Chrome for Linux64 -> https://support.google.com/chrome/a/answer/9025903?hl=de

## Installation

Run the following commands to install the required packages and libraries:

```sh
sudo apt-get update
sudo apt-get uppgrade
sudo apt-get install -y libxss1 libappindicator1 libindicator7
pip install -U selenium webdriver_manager
```
## Usage
Replace the username and password variables in the script with your Instagram account credentials. Adjust the number of users you want to unfollow in the script by changing the range value. Run the script with the following command:

```sh
python3 unfollow.py
```
The script uses random time intervals between 3-12 seconds for each action to mimic human behavior and minimize the risk of getting blocked.

⚠️ **Be careful**, as you can be blocked. I have tested this configuration, and after 25 unfollows, you may get a warning. If you perform too many actions too often, you may get banned. It's best to limit the number of unfollows to 15 and use a cron job with 2 -4 hours intervals to work effectively. ⚠️


## Set up a cron job on Unix/Linux-based systems and macOS
- Open the Terminal.
- Enter crontab -e to edit your crontab file.
Add the following line at the end of the file:
```bash
0 */2 * * * * /usr/bin/python3 /path/to/script.py
```
Replace /usr/bin/python3 with the path to your Python installation and /path/to/script.py with the path to your script.

## Important ⚠️
Please note that the XPath selectors for the Unfollow and Confirm Unfollow buttons and Confirm Cookies might change over time due to updates in Instagram's web interface. Before submitting any issues or reporting bugs, please verify that the current XPath values in the script are still valid and update them if necessary. You can find the relevant XPath values in the script under the variables unfollow_buttons_xpath, confirm_unfollow_xpath and confirm_cookies_xpath.

## Disclaimer
⚠️ This script is for educational purposes and personal use only ⚠️ The user is responsible for complying with Instagram's terms of service and any applicable laws. The author of this script is not responsible for any consequences resulting from the use or misuse of this script.


Copyright by Volkan Kücükbudak
