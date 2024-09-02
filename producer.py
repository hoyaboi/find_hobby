#!C:\Users\minjun\anaconda3\python.exe
# -*- coding: UTF-8 -*-
print("Content-type:text/html")
print()

import script
import pymysql

conn = pymysql.connect(host="localhost", user="root", password="821023", db="project")
curs = conn.cursor()
sql = "select * from producer;"
curs.execute(sql)
rows = curs.fetchall()

desc = ''
for n in range(len(rows)) :
    desc += '<p><strong>%s  -  </strong>%s</p>' % (rows[n][1], rows[n][2])

description = '<div class="producer"><h2>Producer</h2>' + desc + '</div>'

script.printHtml(description)
