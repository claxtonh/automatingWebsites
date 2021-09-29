import requests

from bs4 import BeautifulSoup

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import datetime

now = datetime.datetime.now()

content = ''

#extracting Reddit News Stories.  This is modified from a freeCodeCamp tutorial for webscraping HackerNews. Youtube link here: https://youtu.be/s8XjEuplx_U
#The original code was modified to scrap Reddit headlines.

def extract_news(url):
    desiredTag ='h3'  ## This is the current tag Reddit uses for it's headlines
    attrs = {} ## This is for filtering, in case the tag
    print('Extracting Reddit News Stories...')
    cnt = ''
    cnt +=('<b>Top Stories:</b>\n'+'<br>'+'-'*50+'<br>\n<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(soup.find_all(desiredTag, attrs)):
        print("got it")
        cnt+= ((str(i+1)+' :: '+tag.text + "\n" + '<br>'))
    return(cnt)

content = extract_news("https://www.reddit.com/")
print(content)


