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

    def boost(self):
        boost_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[2]/div/div/button')
        boost_btn.click()
        close_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]')
        close_btn.click()

    def auto_swipe(self):
        self.i = 0
        while True:
            sleep(1)
            try:
                if (self.i != 25):
                    self.like()
                else:
                    self.dislike()
                    self.i = 0
                self.i += 1
                
            except Exception:
                self.close_noninter_popup()

    #closing desktop popup 
    def close_noninter_popup(self):
        noninter_btn = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        noninter_btn.click()

bot = TinderBot()
bot.login()
#bot.auto_swipe()