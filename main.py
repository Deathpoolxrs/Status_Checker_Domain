import os
import sys
import warnings
from requests import Session
from concurrent.futures import ThreadPoolExecutor


def sendreq(url):
    x = s.head(url, verify=False ,timeout=4)
    print(str(x.status_code)+" "+str(url))
    
    
warnings.filterwarnings('ignore', message='Unverified HTTPS request')

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '\
                         'AppleWebKit/537.36 (KHTML, like Gecko) '\
                         'Chrome/75.0.3770.80 Safari/537.36'}
s = Session()
s.headers.update(headers)

with ThreadPoolExecutor(max_workers=10) as executor:
    filname=str(input("Please Enter File Path : "))
    with open(filname) as f:
        for lines in f:
            stripline= lines.rstrip()
            url ="https://"+stripline
            executor.submit(sendreq,url)




