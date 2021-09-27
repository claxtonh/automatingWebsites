import requests
from bs4 import BeautifulSoup
import re
import sys

if len(sys.argv) >1:
    url = sys.argv[1]
else:
    sys.exit("Error: Please enter the URL")


r = requests.get(url)

print("Download about to start")

soup = BeautifulSoup(r.content, features="lmxl")

for val in soup.findAll("script"):
    if(re.search("talkPage.init", str(val))) is not None:
        result = str(val)