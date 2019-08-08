import urllib.request
from bs4 import BeautifulSoup
import time

a = {}
tt = 0
for i in range(200,400):
    for j in range(0,300):
        url = "https://www.ithome.com/0/"+str(i)+'/'+str(j)+".htm"

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
            node = soup.find('a',rel="external nofollow")
            if node == None:
                continue
            tmp = node.get_text()
            if tmp in a:
                a[tmp] += 1
            else:
                a[tmp] = 1
    for k,v in a.items():
        print(str(v)+' :'+k)
    print('-------------------------- '+str(i)+' timeout:'+str(tt))
    

