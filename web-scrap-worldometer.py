# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 20:42:32 2020

@author: Teruya Kimura
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

website_url = requests.get('https://www.worldometers.info/coronavirus/').text
soup = BeautifulSoup(website_url,'lxml')

countries_table = soup.find('table',{'id':'main_table_countries_today'})
table_body = countries_table.find('tbody')
rows = table_body.find_all('tr')
data_rows = []
data_table = []

for row in rows:
    for td in row.find_all('td'):
        if(td.find('a', {'class':'mt_a'})):
            data_rows.append(td.find('a', {'class':'mt_a'}).contents)
        else:    
            data_rows.append(td.contents)
    data_table.append(data_rows)
    data_rows = []

dataset = pd.DataFrame(data_table, columns=["Country, Others","Total Cases","New Cases","Total Deaths",\
                                       "New Deaths","Total Recovered","Active Cases","Serious, Critical","Tot Cases/1M pop"])
    