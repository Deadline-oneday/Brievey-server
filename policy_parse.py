from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.parse import quote
from time import *
import datetime
import re


def Set_category(keyword):              #category 설정
    if keyword == "교육":
        category = 13820
    elif keyword == "교통":
        category = 13820
    elif keyword == "일자리":
        category = 13823
    elif keyword == "환경":
        category = 13816
    elif keyword == "녹지":
        category = 13824
    elif keyword == "시민복지":
        category = 13812
    elif keyword == "도시안정":
        category = 13815
    elif keyword == "문화관광":
        category = 13817

    return category


def Seoul_parse(keyword,pageindex):
    crwal_check = 1
    data = {}
    now = datetime.datetime.now()
    category = Set_category(keyword)

    #driver = webdriver.Chrome('/Users/oonja/Downloads/chromedriver_win32/chromedriver.exe')
    driver = webdriver.PhantomJS('/Users/oonja/Downloads/phantomjs-2.1.1-windows/bin/phantomjs.exe')
    url = ("http://opengov.seoul.go.kr/policy/clas/"+str(category)+"?field_policy_year_value=All"
           "&search=&items_per_page=50&page="+str(pageindex)+"&policy_year=All&policy_done=All")
    driver.implicitly_wait(0.1)

    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')

    driver.find_element_by_id("")
    print(soup)

Seoul_parse("교통",1)

