import os
import time
import telegram
import sqlite3
import datetime
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument('headless')                                                                                              # 크롬창을 새롭게 켜지 않고 크롤링을 진행하는 옵션
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")                                                                                           # GPU 가속 방지

#1300808127:AAE1bi5_bLGEBRfYWJa3D9J2_SsKcpfkKmo
bot = telegram.Bot(token='1241503130:AAE4OoAaUKdJ8SRRR5CHYFjPqc05slveQWo')                                                    # 채팅방 봇 토근
chat_id = -1001442438142                                                                                                      # chat_id를 통해 해당 봇에게 메세지를 보내게 할 수 있음.

# Find the target string, return list
def findstrall( findlist, target ):
    ret = []
    for i in findlist:
        ret.append( i.get(target) )
    return ret

def CHECK( boardtype, title ):
    sql1 = "select * from bottest where boardtype=? and title=?"                                                              # 매칭 되는 것이 있는지 Query를 날림. 제목을 기준으로 검색
    cur.execute(sql1, (boardtype, title))
    result = cur.fetchall()                                                                                                   # return type: list
    if( len(result) == 0 ): return 1                                                                                          # No Match Case 
    else: return 0
    
def UpdateMsg( boardtype, title, origin, link, date ):
    sql = "insert into bottest(boardtype, title, link, date) values (?,?,?,?)"
    for A, B, C in zip( title, link, date ):
        if( CHECK(boardtype, A.text) ):                                                                                       # DB에 없는 공지를 찾았을 때
            if( len(C.text.strip()) <= 5 ):                                                                                   # YYYY.MM.DD 형태가 아닐 경우
                nowtime = datetime.datetime.now().strftime('%H:%M')
                if( C.text.strip() < nowtime ):
                    bot.sendMessage(chat_id=chat_id, text=A.text + ' ' + origin+B + ' ' + datetime.datetime.now().strftime("%Y.%m.%d") )
                    cur.execute(sql,(boardtype, A.text, origin+B, datetime.datetime.now().strftime("%Y.%m.%d")))                           
                    conn.commit()
                else:
                    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
                    bot.sendMessage(chat_id=chat_id, text=A.text + ' ' + origin+B + ' ' + yesterday.strftime('%Y.%m.%d') )
                    cur.execute(sql,(boardtype, A.text, origin+B, yesterday.strftime('%Y.%m.%d') ))                           
                    conn.commit()
            else:
                bot.sendMessage(chat_id=chat_id, text=A.text + ' ' + origin+B + ' ' + C.text )                     
                cur.execute(sql,(boardtype, A.text, origin+B, C.text))                            
                conn.commit()

# boardtype: 0-upbit, 1-bithumb, 2-korbit, 3-coinone
# Crawling Function
def process( URL, boardtype ):
    driver = webdriver.Chrome('C:/Users/sunri/chromedriver', chrome_options=options)
    driver.get( URL )
    wait = WebDriverWait(driver, 10)                                                                                          # 보안창 때문에 너무 빨리 크로링하면 보안 페이지가 크롤링됨.
    if( boardtype == 0 ): element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'lAlign')))                         # 로딩이 완전히 될 때까지 기다리는 것
    if( boardtype == 3 ): element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'info-list')))
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    if( boardtype == 0 ):
        title = soup.select( 'td.lAlign > a' )
        title.pop(0)
        link = findstrall( title, 'href' )
        origin = "https://upbit.com"
        date = soup.select( 'tr > td:nth-child(2)' )
        UpdateMsg(boardtype, title, origin, link, date )
                
    elif( boardtype == 1 ):
        title = soup.select( 'tr > td.one-line' )
        date = soup.select( 'tr > td:nth-child(3)' )
        link = findstrall( soup.select('tbody > tr'), 'onclick' )
        link_tail = []
        for i in link:
            link_tail.append( i[15:22] )
        origin = "https://cafe.bithumb.com/view/board-contents/"
        UpdateMsg(boardtype, title, origin, link_tail, date )

    elif( boardtype == 2 ):
        title = soup.select( 'header > h1.post-title > a' )
        date = findstrall( soup.select('header > a > time'), 'datetime' )
        link = findstrall( title, 'href' )
        date_tail = [] 
        for i in date:
            date_tail.append( i[:10].replace("-",".",2) )

        sql = "insert into bottest(boardtype, title, link, date) values (?,?,?,?)"
        for A, B, C in zip( title, link, date_tail ):
            if( CHECK(boardtype, A.text) ):
                bot.sendMessage(chat_id=chat_id, text=A.text + ' ' + B + ' ' + C )                     
                cur.execute(sql,(boardtype, A.text, B, C))                            
                conn.commit()

    elif( boardtype == 3 ):
        title = soup.select( 'landing-main-notice-info > ul > li > a > div > p.info-title > span.info-title-text' )
        date = soup.select( 'landing-main-notice-info > ul > li > a > span' )
        link = findstrall( soup.select( 'landing-main-notice-info > ul > li > a' ), 'href' )
        origin = "https://coinone.co.kr"
        UpdateMsg(boardtype, title, origin, link, date )

while True:
    conn = sqlite3.connect("C:/Users/sunri/notice/test.db")
    cur = conn.cursor()
    process( 'https://upbit.com/service_center/notice', 0 )
    process( 'https://cafe.bithumb.com/view/boards/43', 1 )
    process( 'https://korbitblog.tumblr.com/', 2 )
    process( 'https://coinone.co.kr/', 3 )
    print( 'TEST END ')
    conn.close()
    time.sleep(600) # 60초(1분)을 쉬어줍니다.

