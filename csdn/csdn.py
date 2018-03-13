import urllib.request

url = "http://blog.csdn.net/mK0vouYv4BwgX190fSd/article/details/78949109"
headers = ("User-Agent","Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read()
fhandle = open("C:\\Users\\acer\\Desktop\\pachong\\csdn\\2.html","wb")
fhandle.write(data)
fhandle.close()
