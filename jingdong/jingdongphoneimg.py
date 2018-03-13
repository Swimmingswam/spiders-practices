import re
import urllib.request,urllib.error
def crawImg(url,page):
	html = urllib.request.urlopen(url).read()
	html = str(html)
	pat1 = '<div id="plist".+? <div class="page clearfix">'
	reasult1 = re.compile(pat1).findall(html)
	reasult1 = reasult1[0]
	pat2 = '<img width="220" height="220" data-img="1" data-lazy-img="//(.+?\.jpg)"> '
	imglist = re.compile(pat2).findall(reasult1)
	print(imglist)
	print(4)
	x = 1
	for imgurl in imglist:
		fname = "C:\\Users\\acer\\Desktop\\pachong\\jingdong\\img\\"+str(page)+str(x)+".jpg"
		imgurl = "http://"+imgurl
		print(5)
		try:
			urllib.request.urlretrieve(imgurl,filename=fname)
			print(1)
		except urllib.error.URLError as e:
			print(2)
			if hasattr(e,"code"):
				x+=1
				
			if hasattr(e,"reason"):
				x+=1
		x +=1
		print(3)
for i in range(1,5):
	url = 'https://list.jd.com/list.html?cat=9987,653,655&page='+str(i)
	crawImg(url,i)
