import urllib.request

file = urllib.request.urlopen("http://www.baidu.com")
data = file.read()
fhandle = open('C:\\Users\\acer\\Desktop\\pachong\\baidu\\1.html',"wb")
fhandle.write(data)
fhandle.close()
print(file.info())
print(file.getcode())
print(file.geturl())
'''
filename = urllib.request.urlretrieve("http://www.baidu.com",filename="C:\\Users\\acer\\Desktop\\pachong\\baidu\\1.html")
'''