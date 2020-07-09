"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import re

homepage = requests.get("https://upbit.com/service_center/notice")
soup = BeautifulSoup(homepage.content, "html5lib")
#print( soup.select('body tr a') )
#test = soup.select('body tr a')
#test = soup.find_all( attrs = {'href' : '#header'}) 

#test = soup.select(".tit5")
#test1 = soup.select(".point")
print( soup )
test = soup.find_all( 'td', {'class':'lAlign'} )
print( test )
"""
"""
test1 = soup.find_all( 'div', {'class':'point'} )

def func( soup1, soup2 ):
    name_list = [] 
    point_list = []
    for i, j in zip( soup1, soup2 ):
        name_list.append( i.get_text() )
        point_list.append( j.get_text() )
    for name, point in zip( name_list, point_list ):
        print( 'Title : ' + name.strip('\n') + ' Point : ' + point )
"""
#func( test, test1 )

#print( test.find( attrs={'href':'/movie/bi*'} ) )

#for i in soup.select('body tr a'):
    #if i.title != None:
    #print( i.title )

#print(soup.select(".title"))

"""
#html = urlopen("http://www.naver.com")
res = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')

bsObject = BeautifulSoup( res.content, 'html5lib' )
book_page = []
for cover in bsObject.find_all('div', {'class':'detail'}):
    link = cover.select('a')[0].get('href')
    book_page.append(link)

for index, url in enumerate( book_page ):
    html = urlopen(url)
    bsObject = BeautifulSoup( html, "html.parser" )
    title = bsObject.find( 'meta', {'property':'rb'})
"""

#print( bsObject )
#print( bsObject.head.find("meta", {"property":"me2:post_tag"}).get('content'))
#print( bsObject.find_all(string='결백') )
"""
for link in bsObject.find_all('a'):
    print(link.text.strip(), link.get('href'))
"""
"""
html = urlopen('http://www.kyobobook.co.kr/bestSellerNew/bestseller.laf')
bsObject = BeautifulSoup(html, "html.parser")



# 책의 상세 웹페이지 주소를 추출하여 리스트에 저장합니다.
book_page_urls = []
for cover in bsObject.find_all('div', {'class':'detail'}):
    link = cover.select('a')[0].get('href')
    book_page_urls.append(link)


# 메타 정보로부터 필요한 정보를 추출합니다.메타 정보에 없는 저자 정보만 따로 가져왔습니다.   
for index, book_page_url in enumerate(book_page_urls):
    html = urlopen(book_page_url)
    bsObject = BeautifulSoup(html, "html.parser")
    title = bsObject.find('div', {'class':'title'}).get('content')
    author = bsObject.find('div',{'class':'author'}).get('content')

    print(index+1, title, author)
"""

"""
import re
text = "에러 1122 : 레퍼런스 오류\n 에러 1033: 아규먼트 오류"
regex = re.compile("에러 1033")
mo = regex.search(text)
if mo != None:
    print(mo.group())
"""
"""
import time
import re
import requests
from bs4 import BeautifulSoup

res = requests.get('https://upbit.com/service_center/press')

soup = BeautifulSoup(res.content, 'html.parser')
#print( soup )
# a 태그이면서 href 속성 값이 특정한 값을 갖는 경우 탐색
link_title = soup.select("body")
print( link_title )

"""
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

driver = webdriver.Chrome('C:/Users/sunri/chromedriver', chrome_options=options)
driver.get('https://upbit.com/service_center/notice')
wait = WebDriverWait(driver, 5)
element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'lAlign')))

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
title = soup.select( 'td.lAlign > a' )
views = soup.select( 'td.rAlign' )
date = soup.select( 'tr > td:nth-child(2)' )

#UpbitLayout > div.subMain > div > section.ty02 > article > div > div.tableB > table > tbody > tr:nth-child(3) > td:nth-child(2)

"""
test = soup.find("td", "rAlign")
print( test )
print( test.find_previous("td") )
"""
"""
#print( notices.next_sibling )

def check( tag ):
    return (not tag.has_attr('class') and not tag.has_attr('id'))

test = soup.find_all( check )
print( test )
"""


for A, B, C in zip(title,views, date):
    print( A.text.strip() )
    print( B.text.strip() )
    print( C.text.strip() )


