#GET /varticle/2023472159/comment/v2?callback=_varticle2023472159commentv2&orinum=10&oriorder=o&pageflag=1&cursor=6290535745866714259&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=9&_=1517649089734 HTTP/1.1
#GET /varticle/1472528692/comment/v2?callback=_varticle1472528692commentv2&orinum=10&oriorder=o&pageflag=1&cursor=6164571380015259407&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=9&_=1517649583146 HTTP/1.1
#{"targetid":"2023472159","parent":"0","time":"1517649073","userid":"512131796","content":"\u671f\u5f85\u7b2c\u4e8c\u90e8\ud83d\ude09","up":"1","pokenum":"0","type":1,"repnum":0,"checkhotscale":"0","checktype":"1","checkstatus":"0","isdeleted":0,"custom":"usertype=0","puserid":"0","orireplynum":"0","voteid":0,"guessid":0,"richtype":"0","rootid":"0","thirdid":"pubsource=mobileupdate&msgid=6537024284672&userid=657631750&cfrom=0&scene=0&datakey=targetid%3D2023472159%26vid%3De0024rd470f%26cid%3D47xswolfi4iamlx%26lid%3D%26type%3D2%26out%3D0%26is_pull_hot_comment%3D1%26has_short_video%3D0&seq=146&ctrid=0","id":"6365481579192155566","indexscore":1517649073549},
#http://video.coral.qq.com/varticle/2023472159/comment/v2?callback=_varticle2023472159commentv2&cursor=6290535745866714259
#"content":"\u671f\u5f85\u7b2c\u4e8c\u90e8\ud83d\ude09"
#orinum=10
#"userid":"762397717"
#"nick":"\u4e00\u8def\u5e73\u5b89"
import urllib.request
import http.cookiejar
import re
vid = "2023472159"
comid = "6290535745866714259"
headers = {
	"Accept":"text/html",
	"Accept-Encoding":"utf-8",
	"User-Agent":"Mozilla/5.0",
	"referer":"qq.com"
}
cjar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
headall = []
for key,value in headers.items():
	item = (key,value)
	headall.append(item)
opener.addheaders = headall
urllib.request.install_opener(opener)
def getdata(vid,comid):
	url = "http://video.coral.qq.com/varticle/"+ vid +"/comment/v2?callback=_varticle"+ vid +"commentv2&cursor="+comid+"&orinum=10"
	data = urllib.request.urlopen(url).read().decode("utf-8")
	return data
useridpat = '"userid":"(.*?)",'
nickpat = '"nick":"(.*?)",'
conpat = '"content":"(.*?)",'
idpat = '"id":"(.*?)",'
for i in range(1,10):
	print("------------------------------------")
	print("第"+str(i)+"页的评论内容")
	data = getdata(vid,comid)
	for i in range(0,10):
		useridlist = re.compile(useridpat,re.S).findall(data)
		nicklist = re.compile(nickpat,re.S).findall(data)
		contentlist = re.compile(conpat,re.S).findall(data)
		idlist = re.compile(idpat,re.S).findall(data)
		try:
			print("用户id是："+eval('u"'+useridlist[i]+'"'))
		except:
			print("用户id是：空")
		try:
			print("用户名称是："+eval('u"'+nicklist[i]+'"'))
		except:
			print("用户名称是：空")
		try:
			print("评论内容是："+eval('u"'+contentlist[i]+'"'))
			print("\n")
		except:
			print("评论内容是：空")
			print("\n")
	comid = idlist[9]