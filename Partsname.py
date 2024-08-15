import requests
from bs4 import BeautifulSoup
url = requests.get('https://www.scrapethissite.com/pages/')
soup = BeautifulSoup(url.text , 'lxml')
partname = soup.find('div' , class_='col-md-6 col-md-offset-3')
print(partname.text.strip())

