import requests
import bs4
from bs4 import BeautifulSoup
import numpy as np
import cv2
import os
from config import Config as cfg


class Sporting(requests.Session):
    def __init__(self,url):
        self.url = url
        super().__init__()

    def request(self,method,headers):
        return super().request(method,self.url,headers = headers)

    @staticmethod
    def valid_board(title):
        return True

#We choose to sort by date
cc = Sporting("https://sfbay.craigslist.org/d/sporting-goods/search/scz/sga?sort=date&")
response  = cc.request("GET",cfg.HEADERS)
html_soup = BeautifulSoup(response.text, 'html.parser')

titles = html_soup.find_all('h3', class_= 'result-heading')
post_URLS = html_soup.find_all('a',class_= 'result-image gallery')

for url in post_URLS:
    print(url['href'], end = "")
    print(url.text.replace("$",""),end = "")

# for title in titles:
#     if cc.valid_board(title.text.lower()):
#         print(title.text.strip())



img = cv2.imread('assets/board1.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

fast = cv2.FastFeatureDetector_create()
fast.setNonmaxSuppression(False)

kp = fast.detect(gray_img, None)
kp_img = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0))

cv2.imshow('FAST', kp_img)
cv2.waitKey()
