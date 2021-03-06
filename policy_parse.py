from selenium import webdriver
from bs4 import BeautifulSoup
import re,json,os


def Set_category(keyword):                                      #category 설정
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
    if not os.path.exists("data/"+keyword+".db"):
        url_list = []
        pageindex = 1
        category = Set_category(keyword)

        url = "http://opengov.seoul.go.kr/"

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
            error = str(title[0])[42:-5]                        #문구 슬라이싱
        except:
            error = "정상적"
            pass

        if(error == "등록된 사업이 없습니다."):                   #등록된 사업이 없을 때 반복문 나가기
            non = {}
            non[keyword+"@0"] = "시정운영 주요 핵심과제 정책 및 100억 이상 예산이 투입되는 대규모 정책이 존재하지 않습니다."
            str_non = json.dumps(non,ensure_ascii=False)
            with open("data/" + keyword + ".db", 'w', encoding='UTF-8', newline='') as f:
                f.write(str_non)
            return
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
        re1 = re.compile("\xa0")
        re2 = re.compile(":")
        re3 = re.compile("\n")
        i = 1
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
            tmp = re1.sub(' ', contents[0].text)
            tmp1 = re2.sub('-', tmp)
            tmp2 = re3.sub('`',tmp1)
            data[keyword+"@"+str(i)] = title[0].text + tmp2
            i+=1

        str_data = json.dumps(data,ensure_ascii=False)                  #Json to string convert
        with open("data/"+keyword+".db", 'w', encoding='UTF-8', newline='') as f:
            f.write(str_data)

    else:
        return

def policy_erase():
    for root, dirs, files in os.walk('data/'):
        for fname in files:
            full_fname = os.path.join(root, fname)
            os.remove(full_fname)

def parse_start():
    category_list = ['Edu','Jobs','Green','Welfare','Tourism','Wonsoon','Trans','Environ']
    for keyword in category_list:
        Seoul_parse(keyword)
