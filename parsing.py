# coding: windows-1251 #
from bs4 import BeautifulSoup as beso
import requests
from config import *
import random

def google_pars(user_request):
    url = googleUrlFoSerch + str(user_request) + "&tbm=isch"
    googleurl = requests.get(url)
    page_soup = beso(googleurl.text, "html.parser")
    return page_soup


def getImg(user_request):
    img = google_pars(user_request)
    img = img('img')
    img = img[random.randrange(0, len(img))]
    img = img.get("src")
    return img