#!C:\Users\minjun\anaconda3\python.exe
# -*- coding: UTF-8 -*-

import cgi
import pymysql

conn = pymysql.connect(host='localhost', user='root', password='821023', db='project')
curs = conn.cursor()

form = cgi.FieldStorage()

name = form['name'].value
description = form['description'].value
q1 = form['q1'].value
q2 = form['q2'].value
q3 = form['q3'].value
q4 = form['q4'].value
q5 = form['q5'].value
type = form['type'].value
imglink = form['imglink'].value

# print(id, name, link, q1, q2, q3, q4, q5, type, imglink) # Confirm Content
sql = '''insert into data (name, description, q1, q2, q3, q4, q5, type, imglink) values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');''' %(name, description, q1, q2, q3, q4, q5, type, imglink)
#print(sql)
curs.execute(sql)
conn.commit()

curs.close()
conn.close()

print('Location: database.html')
print()
