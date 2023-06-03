import bs4
import requests 

subpages=["1","2","3","4"]
names=[]

for no in subpages:
    url='https://www.superherodb.com/naruto/900-1037/?page_nr='+no
    response =requests.get(url)

    soup = bs4.BeautifulSoup(response.content,"lxml")

    divs=soup.find_all('div',{"class":"shdbcard3 cat-10"})

    for div in divs:
        anchor=div.find("a")
        names.append(anchor["title"])
        
with open('names.txt', 'w') as f:
    for name in names:
        f.write(name)
        f.write("\n")

    