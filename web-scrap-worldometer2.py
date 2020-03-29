# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 21:55:07 2020

@author: Teruya Kimura
"""
from bs4 import BeautifulSoup
import pandas as pd
import requests
import sqlite3
import json

# Funcao que utiliza o metodo read_html do pandas para retornar um DataFrame
def get_Dataset_by_url(url):
    header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
    }
    r = requests.get(url, headers=header)
    tables = pd.read_html(r.text)
    return tables

# Transforma o html e armazena como uma variável
def get_beautifulSoup(url):
    website_url = requests.get(url).text
    return BeautifulSoup(website_url,'lxml')

# Transforma o DataFrame do Pandas em JSON
def transform_json(dataset):
    return dataset.to_json(orient='index')

# Cria as tabelas do banco de dados, se já existe, ele apenas ignora
def create_db():
    c.execute("CREATE TABLE IF NOT EXISTS requests (j_son text)")

# Insere as informações de quaisquer tabelas extraidas
def insert_info(json_data):
    c.execute("INSERT INTO requests VALUES (?)", [json_data])

if __name__ == '__main__':
    conection = sqlite3.connect('example.db', isolation_level=None)
    c = conection.cursor()
    urlWorldometer = 'https://www.worldometers.info/coronavirus/'
    urlCOVID_UFV_CSV = 'https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-total.csv'
    tables = get_Dataset_by_url(urlWorldometer)
    json_data = transform_json(tables[0])
    create_db()
    #insert_info(json_data)
    website_url = requests.get('https://www.worldometers.info/coronavirus/').text
    covid_ufv_csv = get_beautifulSoup(urlCOVID_UFV_CSV)
    print(covid_ufv_csv.find('p').contents)