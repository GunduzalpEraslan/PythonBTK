from twitterUserInfo import username,password
from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
import time
from selenium.webdriver.common.by import By

class Twitter:
    def __init__(self,username,password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option("prefs",{"intl.accept_languages":"en,en_US"})
        self.browser = webdriver.Chrome("chromedriver.exe",chrome_options=self.browserProfile)
        self.username = username
        self.password = password

    def SignIn(self):
        self.browser.get("https://twitter.com/login")
        time.sleep(3)
        usernameInput = self.browser.find_element(By.XPATH,"//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input")
        self.browser.find_element(By.CSS_SELECTOR,"#react-root > div > div > div > main > div > div > div > div.css-1dbjc4n.r-6koalj.r-16y2uox > div.css-1dbjc4n.r-16y2uox.r-1jgb5lz.r-13qz1uu > div > div.css-18t94o4.css-1dbjc4n.r-1sw30gj.r-42olwf.r-sdzlij.r-1phboty.r-rs99b7.r-ywje51.r-usiww2.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr.r-13qz1uu").click()
        passwordInput = self.browser.find_element((By.XPATH,"//*[@id='react-root']/div/div/div/main/div/div/div/div[2]/div[2]/div[1]/div/div/div/div[3]/div/label/div/div[2]/div[1]/input"))


        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)

        btnSubmit = self.browser.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div').click()

        time.sleep(2)
        
twitter = Twitter(username,password)
twitter.SignIn()
