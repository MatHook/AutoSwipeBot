from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

from secrets import username, password

class TinderBot():
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--window-size=700,800")
        self.driver = webdriver.Chrome(chrome_options = chrome_options)

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(2)

        fb_b_btn = bot.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/span/div[2]/button')
        fb_b_btn.click()

        #switch windows 
        base_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1])

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(username)

        pass_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pass_in.send_keys(password)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        self.driver.switch_to_window(base_window)

        sleep(2)

        alw_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        alw_btn.click()

        sleep(2)

        ntf_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
        ntf_btn.click()

    #like function
    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/button[3]')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/button[1]')
        dislike_btn.click()

    def superlike(self):
        superlike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/button[2]')
        superlike_btn.click()
        sleep(0.5)
        close_superlike_popup_btn = bot.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]')
        close_superlike_popup_btn.click()


    def boost(self):
        boost_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[2]/div/div/button')
        boost_btn.click()
        sleep(0.5)
        close_boost_popup_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]')
        close_boost_popup_btn.click()

    def auto_swipe(self):
        from random import random
        self.boost()
        while True:
            sleep(1)
            try:
                rand = random()
                if rand < .7:
                    self.like()
                    print('Chance of like: {}'.format(rand))
                elif rand >= .1 and rand <= .11:
                    self.superlike()
                    print('Chance of SUPERLIKE: {}'.format(rand))
                else:
                    self.dislike()
                    print('Chance of dislike: {}'.format(rand))

            except Exception:
                try:
                    self.close_noninter_popup()
                except Exception:
                    self.close_match_popup()

    #closing desktop popup 
    def close_noninter_popup(self):
        noninter_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        noninter_btn.click()

    #closing match popup
    def close_match_popup(self):
        match_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/a')
        match_btn.click()

bot = TinderBot()
bot.login()
#bot.auto_swipe()