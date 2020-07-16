import sqlite3
import telegram
import datetime

# Find the target string, return list
def findstrall( findlist, target ):
    ret = []
    for i in findlist: ret.append( i.get(target) )
    return ret

def CHECK( boardtype, title ):
    con1 = sqlite3.connect("C:/Users/sunri/notice/test.db")
    cur1 = con1.cursor()
    sql1 = "select * from bottest where boardtype=? and title=?"     # 매칭 되는 것이 있는지 Query를 날림. 제목을 기준으로 검색
    cur1.execute(sql1, (boardtype, title))
    result = cur1.fetchall()                                         # return type: list
    con1.close()
    if( len(result) == 0 ): return 1                                 # No Match Case 
    else: return 0
    
def UpdateMsg( boardtype, title, origin, link, date ):
    #1300808127:AAE1bi5_bLGEBRfYWJa3D9J2_SsKcpfkKmo
    bot1 = telegram.Bot(token='1241503130:AAE4OoAaUKdJ8SRRR5CHYFjPqc05slveQWo')                                                    # 채팅방 봇 토근
    chat_id1 = -1001442438142                                                                                                      # chat_id를 통해 해당 봇에게 메세지를 보내게 할 수 있음.

    sql2 = "insert into bottest(boardtype, title, link, date) values (?,?,?,?)"
    con2 = sqlite3.connect("C:/Users/sunri/notice/test.db")
    cur2 = con2.cursor()
    for A, B, C in zip( title, link, date ):
        if( CHECK(boardtype, A.text) ):                                                                                       # DB에 없는 공지를 찾았을 때
            if( len(C.text.strip()) <= 5 ):                                                                                   # YYYY.MM.DD 형태가 아닐 경우
                nowtime = datetime.datetime.now().strftime('%H:%M')
                if( C.text.strip() < nowtime ):
                    bot1.sendMessage(chat_id=chat_id1, text=A.text + ' ' + origin+B + ' ' + datetime.datetime.now().strftime("%Y.%m.%d") )
                    cur2.execute(sql2,(boardtype, A.text, origin+B, datetime.datetime.now().strftime("%Y.%m.%d")))                           
                    con2.commit()
                else:
                    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
                    bot1.sendMessage(chat_id=chat_id1, text=A.text + ' ' + origin+B + ' ' + yesterday.strftime('%Y.%m.%d') )
                    cur2.execute(sql2,(boardtype, A.text, origin+B, yesterday.strftime('%Y.%m.%d') ))                           
                    con2.commit()
            else:
                bot1.sendMessage(chat_id=chat_id1, text=A.text + ' ' + origin+B + ' ' + C.text )                     
                cur2.execute(sql2,(boardtype, A.text, origin+B, C.text))                            
                con2.commit()
    con2.close()