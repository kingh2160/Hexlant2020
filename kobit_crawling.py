from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

driver = webdriver.Chrome('C:/Users/sunri/chromedriver', chrome_options=options)
driver.get('https://www.korbit.co.kr/notice/')
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'styled__Tr-l4nq3x-4.gyfcrI')))

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
korbit_link = "https://korbitblog.tumblr.com/"

title = soup.select( 'tbody > tr > td:nth-child(2)' )
date = soup.select( 'tbody > tr > td:nth-child(3)' )

#gatsby-focus-wrapper > div.styled__StyledHigherOrderLayout-j5ea81-0.irzAoW > main > div > div.styled__ListWrapper-sc-1bjyztx-1.hTTZAD > div > table > tbody > tr.styled__Tr-l4nq3x-4.gyfcrI > td:nth-child(2)#gatsby-focus-wrapper > div.styled__StyledHigherOrderLayout-j5ea81-0.irzAoW > main > div > div.styled__ListWrapper-sc-1bjyztx-1.hTTZAD > div > table > tbody > tr.styled__Tr-l4nq3x-4.gyfcrI > td:nth-child(3)
#gatsby-focus-wrapper > div.styled__StyledHigherOrderLayout-j5ea81-0.irzAoW > main > div > div.styled__ListWrapper-sc-1bjyztx-1.hTTZAD > div > table > tbody > tr.styled__Tr-l4nq3x-4.gyfcrI > td:nth-child(3)#gatsby-focus-wrapper > div.styled__StyledHigherOrderLayout-j5ea81-0.irzAoW > main > div > div.styled__ListWrapper-sc-1bjyztx-1.hTTZAD > div > table > tbody > tr:nth-child(2) > td:nth-child(3)
#gatsby-focus-wrapper > div.styled__StyledHigherOrderLayout-j5ea81-0.irzAoW > main > div > div.styled__ListWrapper-sc-1bjyztx-1.hTTZAD > div > table > tbody > tr.styled__Tr-l4nq3x-4.gyfcrI > td:nth-child(2)
#gatsby-focus-wrapper > div.styled__StyledHigherOrderLayout-j5ea81-0.irzAoW > main > div > div.styled__ListWrapper-sc-1bjyztx-1.hTTZAD > div > table > tbody > tr.styled__Tr-l4nq3x-4.gyfcrI > td:nth-child(3)
#gatsby-focus-wrapper > div.styled__StyledHigherOrderLayout-j5ea81-0.irzAoW > main > div > div.styled__ListWrapper-sc-1bjyztx-1.hTTZAD > div > table > tbody > tr:nth-child(2) > td:nth-child(2)
#gatsby-focus-wrapper > div.styled__StyledHigherOrderLayout-j5ea81-0.irzAoW > main > div > div.styled__ListWrapper-sc-1bjyztx-1.hTTZAD > div > table > tbody > tr:nth-child(2) > td:nth-child(2)
#gatsby-focus-wrapper > div.styled__StyledHigherOrderLayout-j5ea81-0.irzAoW > main > div > div.styled__ListWrapper-sc-1bjyztx-1.hTTZAD > div > table > tbody > tr:nth-child(3) > td:nth-child(2)

for A, B in zip( title, date ):
    print( A.text.strip() )
    print( B.text.strip() )


"""
title = soup.select( 'td.lAlign > a' )
views = soup.select( 'td.rAlign' )
date = soup.select( 'tr > td:nth-child(2)' )


for A, B, C in zip(title,views, date):
    print( A.text.strip() )
    print( B.text.strip() )
    print( C.text.strip() )
"""

