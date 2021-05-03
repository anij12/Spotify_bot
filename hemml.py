from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys

class bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.base_url = 'https://open.spotify.com/'
        self.bot = webdriver.Chrome(r"D:/python/chromedriver.exe")
        self.play()


    def play(self):
        self.bot.get(self.base_url)
        time.sleep(3)
        self.bot.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[1]/header/div[5]/button[2]').click()
        time.sleep(7)
        self.bot.find_element_by_xpath('//*[@id="login-username"]').send_keys(self.username)
        self.bot.find_element_by_xpath('//*[@id="login-password"]').send_keys(self.password)
        self.bot.find_element_by_xpath('//*[@id="login-password"]').send_keys(Keys.RETURN)
        time.sleep(7)
        self.bot.find_element_by_xpath('//*[@id="onetrust-close-btn-container"]/button').click()
        time.sleep(4)
        self.bot.find_element_by_xpath('//*[@id="main"]/div/div[2]/div[2]/footer/div/div[2]/div/div[1]/button[3]').click()
        time.sleep(10)

if __name__ == "__main__":
    BOT = bot("aniruddhajoshi12@gmail.com","9920959596Aj")