import os
import time

from InstaFollower import InstaFollower

chrome_driver_path = os.environ['MY_DRIVER']
SIMILAR_ACCOUNT = "khloekardashian"
USERNAME = os.environ['MY_USERNAME']
PASSWORD = os.environ['MY_PASSWORD']

INSTAGRAM_URL = "https://www.instagram.com/accounts/login/"
PAGE_URL = f"https://www.instagram.com/{SIMILAR_ACCOUNT}/"

bot = InstaFollower(chrome_driver_path)
bot.login(INSTAGRAM_URL, USERNAME, PASSWORD)
time.sleep(5)
bot.find_followers(PAGE_URL)
bot.follow()



