# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 22:02:37 2020

@author: Teruya Kimura
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import lxml.html
import time

driver = webdriver.Chrome()

## Colunas que serão utilizadas no dataset ##                 

UF=[] #Estados do Brasil
casosSuspeitos=[] #Numero de casos suspeitos
porcentagemSuspeitos=[] #Porcentagem de casos supeitos
casosConfirmados=[] #Numero de casos confirmados
porcentagemConfirmados=[] #Porcentagem de casos confirmados
casosDescartados=[] #Numero de casos descartados
porcentagemDescartados=[] #Porcentagem de casos descartados
casosObito=[] #Numero de casos que levaram a óbito
porcentagemObito=[] #Porcentagem de casos que levaram a óbito
total=[] #soma com valor total de casos
             
driver.get("http://plataforma.saude.gov.br/novocoronavirus/#COVID-19-world")

content = driver.page_source
soup = BeautifulSoup(content, 'lxml.html')

time.sleep(10)

for a in soup.findAll('div', attrs={'id':'BRTableByData'}):
    print(a)
    
driver.quit()