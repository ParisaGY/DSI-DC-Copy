#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 12:23:24 2016

@author: generalassembly
"""
import requests
url = "http://www.abrahamlincolnonline.org/lincoln/speeches/quotes.htm"
r = requests.get(url)


r.status_code

from bs4 import BeautifulSoup
b = BeautifulSoup(r.text)

quotes = b.find_all(name='p') 

b.find(name='p').find_all(name='b')


for quote in quotes:
    print(quote.find(name='b'))