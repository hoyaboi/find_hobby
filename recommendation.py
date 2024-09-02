#!C:\Users\minjun\anaconda3\python.exe
# -*- coding: UTF-8 -*-
print("Content-type:text/html")
print()

import cgi
import pymysql
import script

conn  = pymysql.connect(host='localhost', user='root', password = '821023', db = 'project')
curs = conn.cursor()
sql = "select * from data"
curs.execute(sql)
rows = curs.fetchall()

form = cgi.FieldStorage()
ques = form['info'].value
name = form['name'].value

list_id = []
q = ques.split(',')
for n in range(len(rows)) :
    if  rows[n][3] == q[0] or rows[n][3] == '3':
        if  rows[n][4] == q[1] or rows[n][4] == '3' or q[1] == '2':
            if  rows[n][5] == q[2] or rows[n][5] == '3' or q[2] == '2':
                if  rows[n][6] == q[3] or rows[n][6] == '3' or q[3] == '2':
                    list_id.append(n)
                elif  rows[n][7] == q[4] or rows[n][4] == '3' or q[4] == '2':
                    list_id.append(n)
            elif  rows[n][6] == q[3] or rows[n][6] == '3' or q[3] == '2':
                if  rows[n][7] == q[4] or rows[n][7] == '3' or q[4] == '2':
                    list_id.append(n)
        elif  rows[n][5] == q[2] or rows[n][5] == '3' or q[2] == '2':
            if  rows[n][6] == q[3] or rows[n][6] == '3' or q[3] == '2':
                if  rows[n][7] == q[4] or rows[n][7] == '3' or q[4] == '2':
                    list_id.append(n)
    elif  rows[n][4] == q[1] or rows[n][4] == '3' or q[1] == '2':
        if  rows[n][5] == q[2] or rows[n][5] == '3' or q[2] == '2':
            if  rows[n][6] == q[3] or rows[n][6] == '3' or q[3] == '2':
                if  rows[n][7] == q[4] or rows[n][7] == '3' or q[4] == '2':
                    list_id.append(n)
liststr = ''
for n in range(len(list_id)) :
    liststr += '''
    <div class="item item%d">
      <a href="%s.py?id=%d">
        <div class="img" style="background-image: url(%s)"></div>
        <span>%s</span>
      </a>
    </div>
    ''' % (n+1, rows[list_id[n]][8], rows[list_id[n]][0], rows[list_id[n]][9], rows[list_id[n]][1])
# print(q)
# print(list_id) # list 확인
description = '<h2>%s님과 어울리는 취미입니다</h2>' %name + '<div class="container">' + liststr + '</div>'

script.printHtml(description)


curs.close()
conn.close()
