import time

from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class InstaFollower:
    def __init__(self, chrome_driver_path):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def login(self, url, username, password):
        self.driver.get(url)

        time.sleep(2)
        username_field = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        password_field = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        username_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.ENTER)

    def find_followers(self, url):
        time.sleep(2)
        self.driver.get(url)
        time.sleep(2)
        followers = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li['
                                                       '2]/a')
        followers.click()

        time.sleep(2)
        modal = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div[2]')
        #''
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        i = 0
        while True:
            i += 1
            follow = self.driver.find_element(By.XPATH, f'/html/body/div[6]/div/div/div[2]/ul/div/li[{i}]/div/div['
                                                        f'2]/button')
            try:
                follow.click()
                time.sleep(1)

            except ElementClickInterceptedException:
                cancel = self.driver.find_element(By.XPATH, '/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel.click()
                time.sleep(1)

