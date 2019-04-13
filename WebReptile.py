import requests
from bs4 import BeautifulSoup
import MySQLdb


def in_sql(list1):
    conn=MySQLdb.connect(host='localhost',user='root',passwd='admin',db='python',charset = "utf8")
    cur=conn.cursor()
    for eachone in list1:
        cur.execute('INSERT INTO t_douban(d_title) VALUES("%s")' %(str(eachone)))

    cur.close()
    conn.commit()
    conn.close()


def get_movie():
    headers={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        'Host':'movie.douban.com'
    }
    moive_list=[]
    for i in range(0,10):
        link='https://movie.douban.com/top250?start='+str(i*25)
        r=requests.get(link,headers=headers,timeout=10)
        print(str(i+1),"页面响应:",r.status_code)

        soup=BeautifulSoup(r.text,"html.parser")
        div_list=soup.find_all('div',class_='hd')
        for each in div_list:
            moive=each.a.span.text.strip()
            moive_list.append(moive)
    in_sql(moive_list)
    return moive_list


movie=get_movie()
print(movie)
