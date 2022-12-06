import requests
from bs4 import BeautifulSoup
# Pandas for storing data!
#import pandas as pd

titles=[] #List to store title
links=[] #List to store link
pointss=[] #List to store rating of the product
dates_created = [] #List to store date created

requests_get = requests.get("https://news.ycombinator.com/?p=20")
#print(requests_get.text)
soup = BeautifulSoup(requests_get.text, 'html.parser')
get_script_tag = str(soup.body.script)
print(soup)
#get_script_tag = str(soup.body.script)

title = aa