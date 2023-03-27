# Best Instagram Unfollower for Debian/Ubuntu (Human Like)

⚠️ **Warning**: This script automates the process of unfollowing users on Instagram. Use it at your own risk. The author takes no responsibility for any consequences resulting from the use of this script. The copyright of this script remains with the author.

If you have knowledge about marketing, then all you need is an unfollower! This script is set up to look like a human, using random time intervals between actions to avoid detection. It's best to run it using a cron job. Important resources for me: https://selenium-python.readthedocs.io/locating-elements.html

## Prerequisites

- Python 3
- pip
- Google Chrome for Linux64 -> https://support.google.com/chrome/a/answer/9025903?hl=de

## Installation

Run the following commands to install the required packages and libraries:

```sh
sudo apt-get update
sudo apt-get install -y libxss1 libappindicator1 libindicator7
pip install -U selenium webdriver_manager
Usage
Replace the username and password variables in the script with your Instagram account credentials. Adjust the number of users you want to unfollow in the script by changing the range value. Run the script with the following command:
```
```sh
python unfollow.py
```
The script uses random time intervals between 3-12 seconds for each action to mimic human behavior and minimize the risk of getting blocked.

Be careful, as you can be blocked. I have tested this configuration, and after 25 unfollows, you may get a warning. If you perform too many actions too often, you may get banned. It's best to limit the number of unfollows to 15 and use a cron job with 10, 15, or 30-minute intervals to work effectively.
