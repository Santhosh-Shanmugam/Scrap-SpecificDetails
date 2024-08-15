import requests
from bs4 import BeautifulSoup
url = requests.get('https://medium.com/@ritupd/web-scraping-countries-and-population-data-using-beautifulsoup-14f8b740c179')
if url.status_code == 200 :
    soup = BeautifulSoup(url.content, 'lxml')
    print("--------------------------------Tittle--------------------------------------")
    link = soup.find('title').text
    print("Page Title : "+link.strip())
    print("\n")
    
    print("------------------------------Headings---------------------------------------------")
    
    headings = soup.find_all('h1')
    print("Respective Headings in Webpages : \n")
    for heading in headings:
        head = heading.text.strip()
        print(f"{head}")
        print("\n")

    print("------------------------------Href Links-------------------------------------------")
    anchor = soup.find_all('a')
    for link in anchor:
        link_ = link.text.strip()
        href = link.get('href')
        print(f"{link_} : {href}")
        print("\n")

else:
    print("Error Occurs While fetching the webpages")