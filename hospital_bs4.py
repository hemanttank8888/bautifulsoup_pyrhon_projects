import re
import requests
from bs4 import BeautifulSoup
from lxml import etree
import html5lib as htmlparser
import pandas as pd
import time
from bs4 import BeautifulSoup
from lxml import etree
import csv
import pandas as pd

url = "https://www.hospitalrecruiting.com/"
r = requests.get(url)
htmlcontent = r.content
soup = BeautifulSoup(htmlcontent, 'html.parser')
dom = etree.HTML(str(soup))
number=1
state=dom.xpath('//select[2]//option')
all_speciality=["https://www.hospitalrecruiting.com/jobs/Physician-Jobs/","https://www.hospitalrecruiting.com/jobs/Addiction-Medicine-Jobs/","https://www.hospitalrecruiting.com/jobs/Allergy-and-Immunology-Jobs/","https://www.hospitalrecruiting.com/jobs/Cardiac-Anesthesiology-Jobs/","https://www.hospitalrecruiting.com/jobs/Critical-Care-Anesthesiology-Jobs/","https://www.hospitalrecruiting.com/jobs/Anesthesiology-Jobs/","https://www.hospitalrecruiting.com/jobs/Anesthesiology-Pain-Management/",'https://www.hospitalrecruiting.com/jobs/Pediatric-Anesthesiology-Jobs/','https://www.hospitalrecruiting.com/jobs/Advanced-Cardiac-Imaging/','https://www.hospitalrecruiting.com/jobs/Advanced-Heart-Failure-Transplant-Cardiology-Jobs/','https://www.hospitalrecruiting.com/jobs/Cardiology-Electrophysiology-Jobs/','https://www.hospitalrecruiting.com/jobs/Cardiology-Jobs/','https://www.hospitalrecruiting.com/jobs/Cardiology-Jobs/','https://www.hospitalrecruiting.com/jobs/Cardiology-Jobs/','https://www.hospitalrecruiting.com/jobs/Dermatology-Jobs/','https://www.hospitalrecruiting.com/jobs/Emergency-Medicine-Jobs/','https://www.hospitalrecruiting.com/jobs/Emergency-Medicine-Jobs/','https://www.hospitalrecruiting.com/jobs/Endocrinology-Jobs/','https://www.hospitalrecruiting.com/jobs/Family-Practice-Jobs/','https://www.hospitalrecruiting.com/jobs/Family-Practice-Sports-Medicine-Jobs/','https://www.hospitalrecruiting.com/jobs/Family-Practice-Obstetrics-Jobs/','https://www.hospitalrecruiting.com/jobs/Gastroenterology-Jobs/','https://www.hospitalrecruiting.com/jobs/Hepatology-Jobs/','https://www.hospitalrecruiting.com/jobs/General-Practice-Jobs/','https://www.hospitalrecruiting.com/jobs/Geriatric-Medicine-Jobs/','https://www.hospitalrecruiting.com/jobs/Hospitalist-Jobs/','https://www.hospitalrecruiting.com/jobs/Infectious-Disease-Jobs/','https://www.hospitalrecruiting.com/jobs/Internal-Medicine-Adolescent-Medicine-Jobs/','https://www.hospitalrecruiting.com/jobs/Internal-Medicine-Critical-Care-Jobs/','https://www.hospitalrecruiting.com/jobs/Internal-Medicine-Jobs/','https://www.hospitalrecruiting.com/jobs/Internal-Medicine-Sleep-Medicine-Jobs/','https://www.hospitalrecruiting.com/jobs/Medical-Director-Jobs/','https://www.hospitalrecruiting.com/jobs/Medical-Geneticist-Jobs/','https://www.hospitalrecruiting.com/jobs/Medical-Pediatrics-Jobs/','https://www.hospitalrecruiting.com/jobs/Nephrology-Jobs/','https://www.hospitalrecruiting.com/jobs/Clinical-Neurophysiology-Jobs/','https://www.hospitalrecruiting.com/jobs/Neurocritical-Care-Jobs/','https://www.hospitalrecruiting.com/jobs/Epilepsy-Neurology-Jobs/','https://www.hospitalrecruiting.com/jobs/Neurology-Jobs/','https://www.hospitalrecruiting.com/jobs/Headache-Neurology-Jobs/','https://www.hospitalrecruiting.com/jobs/Neurology-Hospitalist-Jobs/','https://www.hospitalrecruiting.com/jobs/Interventional-Neurology-Jobs/','https://www.hospitalrecruiting.com/jobs/Movement-Disorder-Neurology-Jobs/','https://www.hospitalrecruiting.com/jobs/Multiple-Sclerosis-Neuroimmunology-Jobs/','https://www.hospitalrecruiting.com/jobs/Neuromuscular-Neurology-Jobs/','https://www.hospitalrecruiting.com/jobs/Pain-Medicine-Neurology-Jobs/','https://www.hospitalrecruiting.com/jobs/Pediatric-Neurology-Jobs/','https://www.hospitalrecruiting.com/jobs/Sleep-Medicine-Neurology-Jobs/','https://www.hospitalrecruiting.com/jobs/Vascular-Neurology-Jobs/','https://www.hospitalrecruiting.com/jobs/Neuromusculoskeletal-Medicine-Jobs/','https://www.hospitalrecruiting.com/jobs/Neurosurgery-Jobs/','https://www.hospitalrecruiting.com/jobs/Pediatric-Neurosurgery/','https://www.hospitalrecruiting.com/jobs/Pediatric-Neurosurgery/','https://www.hospitalrecruiting.com/jobs/Neurosurgery-Spine-Jobs/','https://www.hospitalrecruiting.com/jobs/OB-GYN-Jobs/','https://www.hospitalrecruiting.com/jobs/Gynecologic-Oncology-Jobs/','https://www.hospitalrecruiting.com/jobs/Gynecology-Jobs/','https://www.hospitalrecruiting.com/jobs/Maternal-Fetal-Medicine-Jobs/','https://www.hospitalrecruiting.com/jobs/Hospitalist-OB-GYN-Jobs/','https://www.hospitalrecruiting.com/jobs/Reproductive-Endocrinology-Jobs/','https://www.hospitalrecruiting.com/jobs/Occupational-Medicine-Jobs/','https://www.hospitalrecruiting.com/jobs/Hematology-Oncology-Jobs/','https://www.hospitalrecruiting.com/jobs/Medical-Oncology-Jobs/','https://www.hospitalrecruiting.com/jobs/Neurology-Oncology-Jobs/','https://www.hospitalrecruiting.com/jobs/Ophthalmology-Jobs/','https://www.hospitalrecruiting.com/jobs/Glaucoma-Ophthalmology-Jobs/','https://www.hospitalrecruiting.com/jobs/Neurology-Ophthalmology-Jobs/','https://www.hospitalrecruiting.com/jobs/Pediatric-Ophthalmology-Jobs/','https://www.hospitalrecruiting.com/jobs/Orthopedic-Foot-and-Ankle-Jobs/','https://www.hospitalrecruiting.com/jobs/Orthopedic-Surgeon-Jobs/','https://www.hospitalrecruiting.com/jobs/Orthopedic-Hand-Surgeon-Jobs/','https://www.hospitalrecruiting.com/jobs/Pediatric-Orthopedic-Surgery-Jobs/','https://www.hospitalrecruiting.com/jobs/Orthopedic-Spine-Surgery-Jobs/','https://www.hospitalrecruiting.com/jobs/Orthopedic-Sports-Medicine-Jobs/','https://www.hospitalrecruiting.com/jobs/Orthopedic-Total-Joint-Surgery-Jobs/','https://www.hospitalrecruiting.com/jobs/Orthopedic-Trauma-Surgery-Jobs/','https://www.hospitalrecruiting.com/jobs/Otolaryngology-Jobs/','https://www.hospitalrecruiting.com/jobs/Pediatric-Otolaryngology-Jobs/','https://www.hospitalrecruiting.com/jobs/Pain-Management-Jobs/','https://www.hospitalrecruiting.com/jobs/Palliative-Care-Jobs/','https://www.hospitalrecruiting.com/jobs/Pathology-Jobs/','https://www.hospitalrecruiting.com/jobs/Pediatric-Adolescent-Medicine-Jobs/','https://www.hospitalrecruiting.com/jobs/Pediatric-Cardiology-Jobs/','https://www.hospitalrecruiting.com/jobs/Pediatric-Critical-Care-Jobs/','https://www.hospitalrecruiting.com/jobs/Developmental-Behavioral-Pediatrician-Jobs/','https://www.hospitalrecruiting.com/jobs/Pediatric-Endocrinology-Jobs/','https://www.hospitalrecruiting.com/jobs/Pediatric-Gastroenterology-Jobs/','https://www.hospitalrecruiting.com/jobs/Pediatric-Jobs/','https://www.hospitalrecruiting.com/jobs/Pediatric-Geneticist-Jobs/','https://www.hospitalrecruiting.com/jobs/Pediatric-Hematology-Oncology-Jobs/','https://www.hospitalrecruiting.com/jobs/Pediatric-Hospitalist-Jobs/','https://www.hospitalrecruiting.com/jobs/Neonatology-Jobs/','https://www.hospitalrecruiting.com/jobs/Pediatric-Nephrology-Jobs/','https://www.hospitalrecruiting.com/jobs/Pediatric-Pulmonology-Jobs/','https://www.hospitalrecruiting.com/jobs/Pediatric-Rheumatology-Jobs/','https://www.hospitalrecruiting.com/jobs/Pediatric-Sleep-Medicine-Jobs/','https://www.hospitalrecruiting.com/jobs/Pediatric-Sports-Medicine-Jobs/','https://www.hospitalrecruiting.com/jobs/Physical-Medicine-and-Rehabilitation-Jobs/','https://www.hospitalrecruiting.com/jobs/Pediatric-Physical-Medicine-and-Rehabilitation-Jobs/','https://www.hospitalrecruiting.com/jobs/Plastic-Surgery-Jobs/','https://www.hospitalrecruiting.com/jobs/Podiatry-Jobs/','https://www.hospitalrecruiting.com/jobs/Addiction-Psychiatrist-Jobs/','https://www.hospitalrecruiting.com/jobs/Psychiatry-Jobs/','https://www.hospitalrecruiting.com/jobs/Child-Psychiatry-Jobs/','https://www.hospitalrecruiting.com/jobs/Geriatric-Psychiatry-Jobs/','https://www.hospitalrecruiting.com/jobs/Pulmonology-Jobs/','https://www.hospitalrecruiting.com/jobs/Pulmonary-Critical-Care-Jobs/','https://www.hospitalrecruiting.com/jobs/Interventional-Pulmonology-Jobs/','https://www.hospitalrecruiting.com/jobs/Pulmonary-Sleep-Medicine-Jobs/','https://www.hospitalrecruiting.com/jobs/Body-Imaging-Radiology-Jobs/','https://www.hospitalrecruiting.com/jobs/Radiology-Breast-Imaging-Jobs/','https://www.hospitalrecruiting.com/jobs/Diagnostic-Radiology-Jobs/','https://www.hospitalrecruiting.com/jobs/Radiology-Jobs/','https://www.hospitalrecruiting.com/jobs/Interventional-Radiology-Jobs/','https://www.hospitalrecruiting.com/jobs/Musculoskeletal-Radiology-Jobs/','https://www.hospitalrecruiting.com/jobs/Neuroradiology-Jobs/','https://www.hospitalrecruiting.com/jobs/Pediatric-Radiology-Jobs/','https://www.hospitalrecruiting.com/jobs/Radiation-Oncology-Jobs/','https://www.hospitalrecruiting.com/jobs/Rheumatology-Jobs/','https://www.hospitalrecruiting.com/jobs/Bariatric-Surgery-Jobs/','https://www.hospitalrecruiting.com/jobs/Breast-Surgery-Jobs/','https://www.hospitalrecruiting.com/jobs/Cardiothoracic-Surgery-Jobs/','https://www.hospitalrecruiting.com/jobs/Cardiovascular-Surgery-Jobs/','https://www.hospitalrecruiting.com/jobs/Colorectal-Surgery-Jobs/','https://www.hospitalrecruiting.com/jobs/Endocrine-Surgery-Jobs/','https://www.hospitalrecruiting.com/jobs/General-Surgery-Jobs/','https://www.hospitalrecruiting.com/jobs/Surgical-Oncology-Jobs/','https://www.hospitalrecruiting.com/jobs/Pediatric-Surgery-Jobs/','https://www.hospitalrecruiting.com/jobs/Thoracic-Surgery-Jobs/','https://www.hospitalrecruiting.com/jobs/Transplant-Surgery-Jobs/','https://www.hospitalrecruiting.com/jobs/Trauma-Surgery-Jobs/','https://www.hospitalrecruiting.com/jobs/Vascular-Surgery-Jobs/','https://www.hospitalrecruiting.com/jobs/Urgent-Care-Jobs/','https://www.hospitalrecruiting.com/jobs/Urology-Jobs/','https://www.hospitalrecruiting.com/jobs/Pediatric-Urology-Jobs/','https://www.hospitalrecruiting.com/jobs/Urogynecology-Jobs/','https://www.hospitalrecruiting.com/jobs/Wound-Care-Jobs/']
all_data=[]
for i in all_speciality:
    
    for j in state:
        country=j.text.replace("-",'').replace(", ","-").replace(".","").replace(" ","-")
        if number>=109:
            continue
        print(number)
        number+=1
        if country=='':
            url=i
        else:
            url=f"{i}{country}/"
        def next_page(page):
            r=requests.get(page)
            htmlcontect=r.content
            soup=BeautifulSoup(htmlcontect,'html.parser')
            tree = etree.HTML(str(soup))
            selected_elements = tree.xpath("//span[@class='action']/a[@class='btn green small radius floatleft']")
            data={}
            for post_url in selected_elements:
                href = post_url.attrib['href']
                r = requests.get(href)
                htmlcontent = r.content
                soup = BeautifulSoup(htmlcontent, 'html.parser')
                dom = etree.HTML(str(soup))
                about = soup.find(id='org_info_container').text.replace("\n", "").replace("\t", "").strip()
                print(about)
                about = re.sub(r'\s{2,}', ' ', about)
                discription=soup.find(class_='text_block job_description job_description_content_container  add_scrollbar').text
                discription = re.sub(r'\s{2,}', ' ', discription)
                company = ''.join(dom.xpath('.//div[@id="job_details_container"]/span[1]/span[2]/a/text()'))
                Specialty = ''.join(dom.xpath('.//div[@id="job_details_container"]/span[2]/span[2]/a/text()'))
                Location = ''.join(dom.xpath(".//div[@id='job_details_container']/span[3]/span[2]/span[1]/text()"))
                Job_Type = ''.join(dom.xpath('.//div[@id="job_details_container"]/span[4]/span[2]/text()')).strip()

                data['Domain']='hospitalrecruiting.com'
                data['href']=href
                data['about']=about
                data['discription']=discription
                data['company']=company
                data['profassion']=Specialty
                data['Location']=Location
                data['Job_Type']=Job_Type
                all_data.append(data)
                data={}
                try:
                    title = ''.join(tree.xpath(".//div[@class='hide-mobile']/a[@class='next page-numbers']/@href"))
                    if title:
                        page=f"{url}{title}"
                        next_page(page)
                        print("||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
                except:
                    pass

        next_page(url)
    number=1
get_data_datafram = pd.DataFrame(all_data)
get_data_datafram.to_csv("hospital_recruting.csv")
