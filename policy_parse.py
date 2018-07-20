from selenium import webdriver
from bs4 import BeautifulSoup
import re,json


def Set_category(keyword):              #category 설정
    if keyword == "Edu":
        category = 13820
    elif keyword == "Trans":
        category = 13819
    elif keyword == "Jobs":
        category = 13823
    elif keyword == "Environ":
        category = 13816
    elif keyword == "Green":
        category = 13824
    elif keyword == "Welfare":
        category = 13812
    elif keyword == "Wonsoon":
        category = 13815
    elif keyword == "Tourism":
        category = 13817

    return category

def Seoul_parse(keyword):
    url_list = []
    pageindex = 1
    hangul = re.compile('[^ \u3131-\u3163\uac00-\ud7a3]+')
    category = Set_category(keyword)

    url = "http://opengov.seoul.go.kr/"

    #driver = webdriver.Chrome('/Users/oonja/Downloads/chromedriver_win32/chromedriver.exe')
    #driver = webdriver.PhantomJS('/Users/oonja/Downloads/phantomjs-2.1.1-windows/bin/phantomjs.exe')
    driver = webdriver.PhantomJS('/root/node_modules/phantomjs/bin/phantomjs')
    url2 = url + "/policy/clas/" + str(
        category) + "?field_policy_year_value=2017&search=&items_per_page=50&page=" + str(
        pageindex) + "&policy_year=All&policy_done=All"

    driver.get(url2)
    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select(
        "#content > div > div.view-empty > table > tbody > tr > td"
    )
    try:
        error = str(title[0])[42:-5]                            #문구 슬라이싱
    except:
        error = "정상적"
        pass

    if(error == "등록된 사업이 없습니다."):                   #등록된 사업이 없을 때 반복문 나가기
        return 0
    else:
        first = soup.select(                                #시작
            "#content > div > div.view-content > table > tbody > tr.odd.views-row-first > td.views-field.views-field-nothing-1 > p.title-ellipsis > a"
        )

        url_list.append(url+first[0].get('href'))
        for list_index in range(2,50):                      #나올 수 있는 최대값
            try:
                middle = soup.select("#content > div > div.view-content > table > tbody > tr:nth-of-type("+str(list_index)+") > td.views-field.views-field-nothing-1 > p.title-ellipsis > a")
                url_list.append(url+middle[0].get('href'))
            except:                                         #더이상 찾아올 데이터가 없음
                break
        pageindex += 1

    data = {}
    i=1
    r = re.compile("\xa0")
    print(url_list)
    for url in url_list:
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.select(
            "#page-title"
        )
        contents = soup.select(
            "#comm-view > div:nth-of-type(3) > div"
        )
        data[keyword+"@"+str(i)] = title[0].text + r.sub('*',contents[0].text)
        i+=1

    str_data = json.dumps(data,ensure_ascii=False)                  #Json to string convert
    print(str_data)
    with open("data/"+keyword+".db", 'w', encoding='UTF-8', newline='') as f:
        f.write(str_data)

