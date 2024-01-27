import threading
import requests
from bs4 import BeautifulSoup
from lxml import etree
import csv
import pandas as pd

url = "https://www.hospitalrecruiting.com/"
r = requests.get(url)
htmlcontent = r.content
soup = BeautifulSoup(htmlcontent, 'html.parser')
dom = etree.HTML(str(soup))
number = 1
state = dom.xpath('//select[2]//option')

all_data = []
lock = threading.RLock()
threads = []

def pages(url):
    r = requests.get(url)
    htmlcontent = r.content
    soup = BeautifulSoup(htmlcontent, 'html.parser')
    tree = etree.HTML(str(soup))
    selected_elements = tree.xpath("//div[@class='col-1 mobile-column']//span[@class='action']/a[1]")
    print(selected_elements)
    data = {}
    for post_url in selected_elements:
        href = post_url.attrib['href']
        r = requests.get(href)
        htmlcontent = r.content
        soup = BeautifulSoup(htmlcontent, 'html.parser')
        dom = etree.HTML(str(soup))
        try:
            description = soup.find(class_='job_description_container').text.replace("\n",'').replace("\t",'').strip()
        except:
            description = None
        try:
            about = soup.find(id='org_info_container').text.replace("\n",'').replace("\t",'').strip()
        except:
            about = None
        print("??????????????????????????????????????????????????????????????????????")
        company = ''.join(dom.xpath('.//div[@id="job_details_container"]/span[1]/span[2]/a/text()'))
        Specialty = ''.join(dom.xpath('.//div[@id="job_details_container"]/span[2]/span[2]/a/text()'))
        Location = ''.join(dom.xpath(".//div[@id='job_details_container']/span[3]/span[2]/span[1]/text()"))
        Job_Type = ''.join(dom.xpath('.//div[@id="job_details_container"]/span[4]/span[2]/text()')).strip()
        data['Domain'] = 'hospitalrecruiting.com'
        data['href'] = href
        data['about'] = about
        data['description'] = description
        data['company'] = company
        data['profession'] = Specialty
        data['Location'] = Location
        data['Job_Type'] = Job_Type
        all_data.append(data)
        data={}

    df = pd.DataFrame(all_data)
    df.to_csv('hospital_data2.csv', index=False)
    next_page = tree.xpath("//div[@id='results_container']//div[@class='hide-mobile']/a[@class='next page-numbers']/@href")
    if next_page:
        print()
        url_page=url.split("?page=")
        page = f"{url_page[0]}{next_page[0]}"
        print(page)
        pages(page)

def scrape_data(url):
    with lock:
        pages(url)

number = 1
for j in state:
    country = j.text.replace("-", '').replace(", ", "-").replace(".", "").replace(" ", "-")
    if number >= 109:
        continue
    print(number)
    number += 1
    try:
        url = f"https://www.hospitalrecruiting.com/jobs/Physician-Jobs/{country}/"
        url = url.replace(" ", "")
    except:
        continue
    thread = threading.Thread(target=scrape_data, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

df = pd.DataFrame(all_data)
df.to_csv('hospital_data2.csv', index=False)
