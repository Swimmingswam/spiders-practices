import urllib.request
httphd = urllib.request.HTTPHandler(debuglevel=1)
httpshd = urllib.request.HTTPSHandler(debuglevel=1)
opener = urllib.request.build_opener(httphd,httpshd)
urllib.request.install_opener(opener)
data = urllib.request.urlopen("http://edu.51cto.com").read()
fhandle = open("C:\\Users\\acer\\Desktop\\pachong\\5.html","wb")
fhandle.write(data)
fhandle.close()

