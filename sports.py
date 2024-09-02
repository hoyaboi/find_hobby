#!C:\Users\minjun\anaconda3\python.exe
# -*- coding: UTF-8 -*-
print("Content-type:text/html")
print('')

import pymysql
import script
import cgi

form = cgi.FieldStorage()

conn  = pymysql.connect(host='localhost', user='root', password = '821023', db = 'project')
curs = conn.cursor()
sql = "select * from data where type='sports'"
curs.execute(sql)
rows = curs.fetchall()

# print(rows) # lsit 확인
if 'id' in form :
    hobbyId = form['id'].value
    Id = 0
    for n in range(len(rows)) :
        if int(hobbyId) == rows[n][0]:
            Id = n
    description = '''
    <div class="container_id">
      <h2>%s</h2>
      <p>%s</p>
    </div>
    ''' % (rows[Id][1], rows[Id][2])
else :
    liststr = ''
    for n in range(len(rows)) :
        liststr += '''
        <div class="item item%d">
          <a href="%s.py?id=%d">
            <div class="img" style="background-image: url(%s)"></div>
            <span>%s</span>
          </a>
        </div>
        ''' % (n+1, rows[n][8], rows[n][0], rows[n][9], rows[n][1])
    description ='<h2>Sports</h2>' + '<div class="container">' + liststr + '</div>'
script.printHtml(description)


curs.close()
conn.close()
