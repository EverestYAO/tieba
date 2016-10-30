#-*- coding: UTF-8 -*-
from urllib.request import Request, urlopen
from urllib.error import URLError,HTTPError
import re
import sys
import pymysql
import time
import urllib.request
import sys  
import json

conn = pymysql.connect(host="localhost",user="root",passwd="root",db="douban",charset="utf8")
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS av')
sql = """CREATE TABLE av( id int primary key not null auto_increment,title text,actor text,comment text,time char(255))"""

cur.execute(sql)


indexnumber=1
for i in range(1,100):
	url='https://avmo.pw/cn/page/%d'%i
	req = Request(url)
	user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit'
	req.add_header('User-Agent' ,user_agent)
	try:
		response = urlopen(req)
	except HTTPError as e:
		print ('The server couldn\'t fulfill the request.')
		print ('Error code:',e.code)
	except URLError as e:
		print('We failed to reach a server.')
		print('Reason:',e.reason)
	html = response.read().decode('utf-8')
	pa=re.compile(r'"movie-box" href="(.*)"')
	link=pa.findall(html)
	print("获取第%d页"%indexnumber)
	indexnumber=indexnumber+1





	for j in link:
		req = Request(j)
		user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit'
		req.add_header('User-Agent' ,user_agent)
		try:
			response = urlopen(req)
		except HTTPError as e:
			print ('The server couldn\'t fulfill the request.')
			print ('Error code:',e.code)
		except URLError as e:
			print('We failed to reach a server.')
			print('Reason:',e.reason)
		html = response.read().decode('utf-8')






		p1 = re.compile(r'<span>(.*)</')
		p2=re.compile(r'<span style="color:#CC0000;">(.*)</span>')
		p3=re.compile(r'src="(.*jpg)"')
		p4=re.compile(r'<span class="header">发行时间:.*</span>(.*)</p>')
		p5=re.compile(r'<h3>(.*)</h3>')
		actor=p1.findall(html)
		fanhao=p2.findall(html)
		pic=p3.findall(html)
		ti=p4.findall(html)
		comment=p5.findall(html)



		sql2='INSERT INTO av VALUES(null,"%s","%s","%s","%s")'
		l2=[]
		l2.append([fanhao,comment,actor,ti])
		cur.executemany(sql2,l2)
		conn.commit()
		for j in comment:
				print("正在写入"+j)
		time.sleep(0.2)




