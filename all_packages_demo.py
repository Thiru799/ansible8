# all_packages_demo.py

import os
import datetime
from pathlib import Path
from typing import List
import six
import urllib3
import certifi
import idna
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from dateutil import parser
import pytz
import sqlalchemy
from O365 import Account
from pywinauto import Application
from selenium import webdriver
import configparser
from configobj import ConfigObj
from cryptography.fernet import Fernet
from fuzzywuzzy import fuzz
import pytest

def web_scraping():
    url = "https://www.python.org/jobs/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    jobs = []
    for job in soup.find_all('h2', class_='listing-company'):
        title = job.text.strip()
        jobs.append({'Title': title})
    df = pd.DataFrame(jobs)
    df.to_excel('python_jobs.xlsx', index=False)
    print("Web scraping and Excel export successful.")

def data_analysis():
    dates = ['2025-01-01', '2025-06-15', '2025-12-31']
    parsed_dates = [parser.parse(date).astimezone(pytz.timezone('Asia/Singapore')) for date in dates]
    df = pd.DataFrame({'Dates': parsed_dates})
    print("Date analysis:")
    print(df)

def database_interaction():
    engine = sqlalchemy.create_engine('sqlite:///example.db')
    with engine.connect() as connection:
        result = connection.execute("SELECT sqlite_version();")
        for row in result:
            print(f"SQLite version: {row[0]}")

def email_integration():
    credentials = ('client_id', 'client_secret')
    account = Account(credentials)
    if account.authenticate(scopes=['basic', 'message_all']):
        print("Authentication successful.")
    else:
        print("Authentication failed.")

def gui_automation():
    app = Application().start("notepad.exe")
    app.UntitledNotepad.Edit.type_keys("Hello, World!", with_spaces=True)
    print("Notepad automation complete.")

def web_automation():
    driver = webdriver.Chrome()  # Ensure chromedriver is in PATH
    driver.get("https://www.python.org")
    print("Browser automation complete.")
    driver.quit()

def config_management():
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'Server': 'localhost', 'Port': '8080'}
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    print("ConfigParser: Configuration written.")

    config_obj = ConfigObj()
    config_obj.filename = 'configobj.ini'
    config_obj['Server'] = 'localhost'
    config_obj['Port'] = '8080'
    config_obj.write()
    print("ConfigObj: Configuration written.")

def cryptographic_operations():
    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(b"Secret message")
    print(f"Encrypted: {token}")
    print(f"Decrypted: {f.decrypt(token)}")

def string_matching():
    ratio = fuzz.ratio("hello world", "hello world!")
    print(f"String similarity ratio: {ratio}")

def miscellaneous_utilities():
    path = Path('example.txt')
    path.write_text('Sample text.')
    print(f"File created at: {path.resolve()}")

    def greet(names: List[str]) -> None:
        for name in names:
            print(f"Hello, {name}!")
    greet(['Alice', 'Bob'])

    print(f"Is 'six' Python 2 compatible? {six.PY2}")

    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    response = http.request('GET', 'https://www.google.com')
    print(f"HTTP response status: {response.status}")

def run_all():
    web_scraping()
    data_analysis()
    database_interaction()
    # email_integration()  # Uncomment after setting up credentials
    # gui_automation()     # Uncomment if running on Windows
    # web_automation()     # Uncomment after setting up WebDriver
    config_management()
    cryptographic_operations()
    string_matching()
    miscellaneous_utilities()

if __name__ == "__main__":
    run_all()
