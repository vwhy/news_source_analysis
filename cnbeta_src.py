import urllib.request
from bs4 import BeautifulSoup
import time

a = {}
tt = 0

for i in [2*i+1 for i in range(250000,350000)]:
	url = "https://www.cnbeta.com/articles/tech/"+str(i)+".htm"

	try:
		html = urllib.request.urlopen(url)
	except urllib.error.HTTPError:
		pass
	except urllib.error.URLError:
		tt += 1
		print('timeout['+str(tt)+']')
		time.sleep(30)
		j-=1
	else:
		soup = BeautifulSoup(html,'html.parser')
		node = soup.find('span',class_="source")
		if node == None:
		    continue
		node1 = node.find('span')
		if node1 == None:
			continue
		tmp = node1.get_text()
		if tmp in a:
			a[tmp] += 1
		else:
			a[tmp] = 1
	if ((i-1)%100) == 0:
		for k,v in a.items():
			print(str(v)+' :'+k)
		print('-------------------------- '+str(i)+' timeout:'+str(tt))
        

