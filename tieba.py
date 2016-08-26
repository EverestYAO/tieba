#-*- coding: UTF-8 -*-
import urllib
import urllib2
import re
import sys
def open_url(url):
	req = urllib2.Request(url)
	user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit'
	headers = {'User-Agent' : user_agent}
	try:page = urllib2.urlopen(req)
	except urllib2.URLError,e:
		print e.reason
		
	html = page.read().decode('utf-8')
	return html
	
def get_pages(url):
	req = urllib2.Request(url)
	user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit'
	headers = {'User-Agent' : user_agent}
	try:page = urllib2.urlopen(req)
	except urllib2.URLError,e:
		print e.reason
	html = page.read().decode('utf-8')
	t = re.compile(r'cur_page":\d,"total_page":(\d*)')
	pa = t.findall(html)
	return pa
	
def get_img(html):
	p = re.compile(r'src="([^"]+\.jpg)"')
	imglist = p.findall(html)
	i = 1
	for each in set(imglist):
		filename = each[-8:]
		try:
			urllib.urlretrieve(each,filename,None)
			print "downloading" + str(i) + u" 张小黄图"
		except:
			print "Unexpected error:", sys.exc_info()[0]
		i+= 1
		
def start():
	a = get_pages(url)
	for x in a:
		for j in range(1,int(x)+1):
			url2 = url[:-1] + str(j) 
			get_img(open_url(url2))
			print '已经爬取了第 ' + str(j) + ' 页'
		

if __name__=='__main__':
	print "百度贴吧可以直接使用"
	url = raw_input('输入网址把: ')
	print url[:-6]
	start()