import pandas as pd
import requests
import sqlite3
import json


def get_Dataset_by_url(url):
#    header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
#    "X-Requested-With": "XMLHttpRequest"
#    }
    r = requests.get(url)
    tables = pd.read_html(r.text)
    return tables

def transform_json(dataset):
    return dataset.to_json(orient='index')

def create_db():
    c.execute("CREATE TABLE IF NOT EXISTS requests (j_son text)")

def insert_info(json_data):
    c.execute("INSERT INTO requests VALUES (?)", [json_data])

if __name__ == '__main__':
    conection = sqlite3.connect('example.db', isolation_level=None)
    c = conection.cursor()
    url = 'https://labs.wesleycota.com/sarscov2/br/'
    tables = get_Dataset_by_url(url)
    for table in tables:
        print(table)
#    json_data = transform_json(tables[0])
#    create_db()
#    insert_info(json_data)