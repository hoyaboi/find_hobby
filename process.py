#!C:\Users\minjun\anaconda3\python.exe
# -*- coding: UTF-8 -*-
print("Content-type:text/html")
print('')

import cgi
import pymysql

conn  = pymysql.connect(host='localhost', user='root', password = '821023', db = 'project')
curs = conn.cursor()
sql = "select * from data"
curs.execute(sql)
rows = curs.fetchall()
print(rows)

form = cgi.FieldStorage()
ques = form["info"].value
list_id = []
q = ques.split(',')
print(q)

for n in range (len(rows)) :
    if  rows[n][3] == q[0] :
        if  rows[n][4] == q[1] :
            if  rows[n][5] == q[2] :
                if  rows[n][6] == q[3] :
                    list_id.append(n)
                elif  rows[n][7] == q[4] :
                    list_id.append(n)
            elif  rows[n][6] == q[3] :
                if  rows[n][7] == q[4]:
                    list_id.append(n)
        elif  rows[n][5] == q[2] :
            if  rows[n][6] == q[3] :
                if  rows[n][7] == q[4] :
                    list_id.append(n)
    elif  rows[n][4] == q[1] :
        if  rows[n][5] == q[2] :
            if  rows[n][6] == q[3] :
                if  rows[n][7] == q[4] :
                    list_id.append(n)

print(list_id)

for n in range (len(list_id)) :
    print(rows[list_id[n]][2])

curs.close()
conn.close()
