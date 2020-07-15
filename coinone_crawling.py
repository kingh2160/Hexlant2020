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
driver.get('https://coinone.co.kr/')
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'info-list')))

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

title = soup.select( 'landing-main-notice-info > ul > li > a > div > p.info-title > span.info-title-text' )
article = soup.select( 'landing-main-notice-info > ul > li > a > div > p.info-summary' )
date = soup.select( 'landing-main-notice-info > ul > li > a > span' )
link = str(soup.select( 'landing-main-notice-info > ul > li > a[href]' ))
originUrl = "https://coinone.co.kr/"

#origin에 answer값 더해주면 댐

answer = []
def findstrall( str, target ):
    idx = -1
    while True:
        idx = str.find(target, idx+1)
        if( idx == -1 ): break
        answer.append(str[idx+6:idx+30])
findstrall( link, 'href' )
print(answer)

#body_inner > landing-main > div.info-section.section-inner > div.crypto-info > landing-main-notice-info > ul > li:nth-child(1) > a > div > p.info-title > span.info-title-text
#body_inner > landing-main > div.info-section.section-inner > div.crypto-info > landing-main-notice-info > ul > li:nth-child(1) > a > div > p.info-summary
#body_inner > landing-main > div.info-section.section-inner > div.crypto-info > landing-main-notice-info > ul > li:nth-child(1) > a > span
#body_inner > landing-main > div.info-section.section-inner > div.crypto-info > landing-main-notice-info > ul > li:nth-child(1) > a
#body_inner > landing-main > div.info-section.section-inner > div.crypto-info > landing-main-project-info > ul > li:nth-child(1) > a

for A, B, C in zip( title, article, date ):
    print( A.text.strip() )
    print( B.text.strip() )
    print( C.text.strip() )

"""
title = soup.select( 'td.lAlign > a' )
views = soup.select( 'td.rAlign' )
date = soup.select( 'tr > td:nth-child(2)' )


for A, B, C in zip(title,views, date):
    print( A.text.strip() )
    print( B.text.strip() )
    print( C.text.strip() )
"""

