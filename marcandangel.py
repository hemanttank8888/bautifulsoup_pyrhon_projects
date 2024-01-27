#Python program to scrape website
#and save quotes from website
import pandas
from concurrent import futures
import requests
from bs4 import BeautifulSoup
import csv
from lxml import etree
URL = "http://www.marcandangel.com/"
all_data=[]

def next_page(URL):
    r = requests.get(URL)
    soup1 = BeautifulSoup(r.content, 'html5lib')
    tree = etree.HTML(str(soup1))
    main_div = soup1.findAll('article') 
    quotes={}
    data_string=''
    for article in main_div:
        title=article.header.h2.text.replace("\n", "").replace("\t", "")
        image_url=article.select_one('div.entry-content p img')['src']
        text_content=article.select_one("div.entry-content").text.replace("\n", "").replace("\t", "")

        if "[Read more…]" in text_content:
            read=article.select_one("div.entry-content p a")['href']

            r = requests.get(read)
            soup = BeautifulSoup(r.content, 'html5lib')
            paragraphs = [paragraph.get_text().replace("\n", "").replace("\t", "") for paragraph in soup.select('div.entry-content p')]
            text_content = ' '.join(paragraphs)
        # print(text_content)
        if image_url is not None:
            data_string += f"{title}|{image_url}|{text_content} "
        else:
            data_string += f"{title}|{text_content} "
    all_data.append(data_string)
    print(URL)

next_page(URL)
with futures.ThreadPoolExecutor(20) as ex:
    for i in range(2,219):
        path=f"https://www.marcandangel.com/page/{i}/"

        ex.submit(next_page,path)
df = pandas.DataFrame(all_data)
df.columns = ["title"]
df.to_csv("marcandangel_data.csv",index=False,header=True)

