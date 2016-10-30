import urllib2
from bs4 import BeautifulSoup

url = 'http://www.qiushibaike.com/hot/'

user_agent = 'Mozilla/5.0 (Windows NT 6.1)'

headers = {'User-agent' : user_agent}

request = urllib2.Request(url,headers= headers)

response = urllib2.urlopen(request)

cat_img = response.read().decode('utf-8')

bs0bj = BeautifulSoup(cat_img,"html.parser")

namelist = bs0bj.findAll('div', "content")

for name in namelist:

	print(name.string)
