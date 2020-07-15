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
driver.get('https://cafe.bithumb.com/view/boards/43')
#wait = WebDriverWait(driver, 5)
#element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'lAlign')))

html = driver.page_source
driver.quit()
soup = BeautifulSoup(html, 'html.parser')
#title = soup.select( 'tr > td.one-line' )
#date = soup.select( 'tr > td:nth-child(3)' )
link = str(soup.select('tr[onclick]'))
answer = []
def findstrall( str, target ):
    idx = -1
    while True:
        idx = str.find(target, idx+1)
        if( idx == -1 ): break
        answer.append(str[idx+23:idx+31])
findstrall( link, 'onclick' )

originurl = "https://cafe.bithumb.com/view/board-contents/"

# originurl에다가 각 list에 있는 숫자들 뒤에 붙여주면 됨.

#dataTables > tbody > tr:nth-child(1) > td.one-line
#dataTables > tbody > tr:nth-child(1) > td:nth-child(3)
#dataTables > tbody > tr:nth-child(2) > td.one-line
#dataTables > tbody > tr:nth-child(2) > td:nth-child(3)
#dataTables > tbody > tr:nth-child(4) > td.one-line
#dataTables > tbody > tr:nth-child(4) > td:nth-child(3)
#dataTables > tbody > tr:nth-child(5)
"""
for A, B in zip( title, date ):
    print( A.text.strip() )
    print( B.text.strip() )
    #print( C.text.strip() )
"""

"""
title = soup.select( 'td.lAlign > a' )
views = soup.select( 'td.rAlign' )
date = soup.select( 'tr > td:nth-child(2)' )


for A, B, C in zip(title,views, date):
    print( A.text.strip() )
    print( B.text.strip() )
    print( C.text.strip() )
"""

