import requests
from bs4 import BeautifulSoup
import html5lib as htmlparser
import pandas as pd

url="https://www.flipkart.com/search?q=mi+phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY"
r=requests.get(url)
htmlcontect=r.content
soup=BeautifulSoup(htmlcontect,'html.parser')
head=soup.find_all(class_="_4rR01T")
head1=[]
for heading in head:
    head1.append(heading.text)
print(head1)

links=soup.find_all(class_='_1fQZEK')
for link in links:
    print(link.get("href"))

page_numbers=soup.find_all(class_="ge-49M")
for page_number in page_numbers:
    url='https://www.flipkart.com'+str(page_number.get("href"))
    print(url)
Rams=[]
head1 = []
Display=[]
Cameras=[]
Battery=[]
num=1
for page_number in page_numbers:

    url = 'https://www.flipkart.com' + str(page_number.get("href"))
    r = requests.get(url)
    htmlcontect = r.content
    soup = BeautifulSoup(htmlcontect, 'html.parser')

    head = soup.find_all(class_="_4rR01T")
    for heading in head:
        head1.append(heading.text)
    links = soup.find_all(class_='_1fQZEK')
    num+=1
    for link in links:
        
        url = 'https://www.flipkart.com' + str(link.get("href"))
        r = requests.get(url)
        htmlcontect = r.content
        soup = BeautifulSoup(htmlcontect, 'html.parser')
        Ram=soup.find_all(class_='_21Ahn-')
        Rams.append(Ram[0].text)
        Display.append(Ram[1].text)
        Cameras.append(Ram[2].text)
        Battery.append(Ram[3].text)
    print(head1)
    print(Rams)
    if num==3:
        break
all=list(zip(head1,Rams,Display,Cameras,Battery))
data=pd.DataFrame(all)
data.to_csv('processed3.csv', mode='a',header=['names','Rams & Roms','Display','Cameras','Battery'], index=False)
print(head1)
print(Rams)
