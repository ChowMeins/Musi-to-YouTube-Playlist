from bs4 import BeautifulSoup
import requests 

URL = "https://feelthemusi.com/playlist/kzuybo"
r = requests.get(URL) 
#print(r.content) 

soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib 

results = soup.find(class_="track")
print(results)