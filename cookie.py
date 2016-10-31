import urllib
import urllib2
import cookielib

filename = 'cookie.txt'
cookie = cookielib.CookieJar()
handler=urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)
reponse = opener.open('http://www.zhihu.com')
for item in cookie:
    print 'Name = ' +item.name
    print 'Value = '+item.value

data={"email":"","password":""}
postdata=urllib.urlencode(data)
loginurl='https://www.zhihu.com/#signin'
request=opener.open(loginurl,postdata)
cookie.save(ignore_discard=True, ignore_expires=True)

geturl='https://www.zhihu.com/people/edit'
result = opener.open(geturl)
filename ='cookie.html'
fobj=open(filename,'w')
fobj.write(result.read())
fobj.close()


