import urllib.request,urllib.parse
url = "http://www.iqianyue.com/mypost/"
postdata = urllib.parse.urlencode({
	"name":"915860430@qq.com",
	"pass":"915860430"
	}).encode('utf-8')
req  = urllib.request.Request(url,postdata)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36")
data = urllib.request.urlopen(req).read()
fhandle = open("C:\\Users\\acer\\Desktop\\pachong\\cookie\\4.html","wb")
fhandle.write(data)
fhandle.close()