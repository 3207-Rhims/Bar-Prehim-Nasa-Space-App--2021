import urllib.request, urllib.parse, urllib.error
import json
import ssl
from bs4 import BeautifulSoup
from pprint import pprint
from json2html import *
from html2csv import *
from requests import *
import re

api_key = False

if api_key is False:
    serviceurl = "   "
else :
    serviceurl = ''

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    #address = input('Enter location: ')
    parms = dict()
   # parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    js = json.loads(data)    
    this=json2html.convert(json = js)
    pprint(this)
    soup=BeautifulSoup(this,"html.parser")
    for link in soup.find_all("td"):
        print("Inner Text: {}".format(link.text))
© 2021 GitHub, Inc.
Terms
Privacy
Security
