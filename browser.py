from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests
import pyautogui
from tkinter import *
from multiprocessing import Pool
from concurrent.futures import ThreadPoolExecutor


# login to website using selenium and get cookies

class twitter_bot:
    def __init__(self):

        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bo
        bot.get('https://www.instagram.com/accounts/login/?hl=tr')
        time.sleep(5)
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.ENTER)

        try:
            time.sleep(7)
            self.bot.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button").click()
        except Exception as e:
            print(e)

    def clicker(self):
        try:
            time.sleep(3)
            self.bot.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
        except Exception as ex:

            print(ex)

    def followuser(self):
        self.bot.get("https://www.instagram.com/invamed.health/")
        time.sleep(5)
        if self.bot.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button").text == "Follow":
            self.bot.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button").click()
            print("Takip edilen kullanıcı" + "invamed.health")
        else:
            print("Kullanıcı zaten Takip  edilmiş")

    def likeBomb(self):
        self.bot.get("https://www.instagram.com/invamed.health/")
        twitter_bot.scrollPage(self)
        list = self.bot.find_elements_by_xpath("//div[contains(@class, 'v1Nh3 kIKUG  _bz0w')]/a")
        list2 = []
        for x in list:
            list2.append(x.get_attribute("href"))
            print("Listeye Eklendi: " + x.get_attribute("href"))
        for x in list2:
            twitter_bot.likePhoto(self, link=x)

    def scrollPage(self):
        SCROLL_PAUSE_TIME = 0.5

        # Get scroll height
        last_height = self.bot.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.bot.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.bot.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

    def likePhoto(self, link):
        self.bot.get(link)
        try:
            self.bot.find_element_by_xpath(
                "/html/body/div[1]/section/main/div/div/article/div[3]/section[1]/span[1]").click()
            print("Fotoğraf beğenildi... Link:" + link)
        except Exception as e:
            print(e)

    def logout(self):
        time.sleep(5)
        self.bot.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span").click()
        time.sleep(5)
        self.bot.find_element_by_xpath(
            "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/div/div/div/div/div/div/div").click()
        time.sleep(5)
        print("cıkış yapılıyor")


