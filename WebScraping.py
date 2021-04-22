#Web Scraping
import requests
from bs4 import BeautifulSoup
import pandas as pd


def extract(page):
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36'}
	url = f'https://www.indeed.com/jobs?q=python+developer&l=Austin%2C+TX&start={page}'
	r = requests.get(url,headers)
	soup = BeautifulSoup(r.content, 'html.parser')
	return soup

def trans(soup):
    divs = soup.find_all('div', class_ = 'jobsearch-SerpJobCard')
    for job in divs:
        title = job.find('a').text.strip()
        company = job.find('span' , class_ = 'company').text.strip()
        try:
            pay = job.find('span', class_ = 'salaryText')
        except:
            pay = ''
        #summary = job.find('div', {'class' : 'summary'}).text.strip()
    
        jobs = {
        'title' : title,
        'company' : company,
        'salary' : pay,
        #'summary' : summary

        }
    

        joblist.append(jobs)
 
    return 


joblist = []
   
for i in range(0,50,10):
    print(f'Getting Page, {i}')
    call = extract(0)
    trans(call)


df = pd.DataFrame(joblist)

print(df.head())
df.to_csv(r'C:\Users\14052\Desktop\Dev\Python_Development\misc\jobs.csv')