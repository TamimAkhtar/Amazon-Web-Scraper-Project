#!/usr/bin/env python
# coding: utf-8

# In[2]:


#import libraries
from bs4 import BeautifulSoup
import requests
import smtplib
import time
import datetime


# In[7]:


#Connect to the Website
URL = 'https://www.amazon.com.tr/LEGO-Ideas-21319-Central-Perk/dp/B07VGGF8DP/ref=sr_1_2?__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3MMQJWUAT90UZ&keywords=formula+1&qid=1669482976&qu=eyJxc2MiOiI1LjUwIiwicXNhIjoiNS4wNCIsInFzcCI6IjMuOTAifQ%3D%3D&sprefix=formula1%2Caps%2C395&sr=8-2'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56"}
#we can get the headers from http://httpbin.org/get

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, 'html.parser')
print(soup1)
#we are printing in all of the html from our variable called page


# In[8]:


soup1 = BeautifulSoup(soup1.prettify() , 'html.parser')
print(soup1)


# In[26]:


#Lets scrape our specific data from the page
title = soup1.find(id = 'productTitle').get_text()
print(title)

price = soup1.find("span", {"class": "a-offscreen"}).get_text()
print(price)


# In[28]:


#We can clean up a bit
price = price.strip()[0:8]
title = title.strip()

print(price)
print(title)


# In[31]:


today = datetime.date.today()
print(today)

import csv
    
header = ['Title' , 'Price' , 'Date']
data = [title,price, today]

with open('AmazonWebScraperDataset.csv' , 'w' , newline='',encoding = 'UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)


# In[32]:


import pandas as pd
df = pd.read_csv(r'C:\Users\lenovo\AmazonWebScraperDataset.csv')
print(df)


# In[35]:


def check_price():
    URL = 'https://www.amazon.com.tr/LEGO-Ideas-21319-Central-Perk/dp/B07VGGF8DP/ref=sr_1_2?__mk_tr_TR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3MMQJWUAT90UZ&keywords=formula+1&qid=1669482976&qu=eyJxc2MiOiI1LjUwIiwicXNhIjoiNS4wNCIsInFzcCI6IjMuOTAifQ%3D%3D&sprefix=formula1%2Caps%2C395&sr=8-2'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.56"}
    
    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, 'html.parser')
            
    soup1 = BeautifulSoup(soup1.prettify() , 'html.parser')
               
    title = soup1.find(id = 'productTitle').get_text()
               
    price = soup1.find("span", {"class": "a-offscreen"}).get_text()
               
    price = price.strip()[0:8]
    title = title.strip()
               
    today = datetime.date.today()
               
    import csv
    
    header = ['Title' , 'Price' , 'Date']
    data = [title,price, today]
               
    
    #We append our new data to the existing data
    with open('AmazonWebScraperDataset.csv' , 'a+' , newline='',encoding = 'UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        
    if(price<500):
        send_email()


# In[36]:


#We will run this every 5 seconds
while(True):
    check_price()
    time.sleep(5)


# In[37]:


df = pd.read_csv(r'C:\Users\lenovo\AmazonWebScraperDataset.csv')
print(df)


# In[ ]:


def send_email():
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo()
    #server.starttls()
    server.ehlo()
    server.login('tamiim.akhtar@gmail.com','xxxxxxxxxxxx')
    
    subject = 'The Lego set you want is now below 500 TRY!!!!!!'
    body = 'Dear Tamim, This is the moment your dream of owning this Lego Set can become a reality, BUCKLE UP'
    
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail('tamiim.akhtar@gmail.com', msg)

