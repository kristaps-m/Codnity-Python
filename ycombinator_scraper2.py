import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")
if response.status_code != 200:
	print("Error fetching page")
	exit()
else:
	content = response.content
#print(content)

soup = BeautifulSoup(response.content, 'html.parser')

all_hrefs = [a for a in soup.find_all(class_="titleline")]
print(len(all_hrefs))

all_scores = [a for a in soup.find_all(class_="score")]
print(len(all_scores))

all_ages = [a for a in soup.find_all(class_="age")]
print(len(all_ages))
#print(all_hrefs[0])
#print(all_hrefs[0].get_text())

if(len(all_hrefs) == len(all_scores) and len(all_scores) == len(all_ages)):
  print("-------------------YES--------------")
else:
  print("-------------------NO--------------")

for href in all_hrefs:
  print(href.a.get("href"))

for href in all_hrefs:
  print(href.get_text())

for score in all_scores:
  print(score.get_text())

for age in all_ages:
  print(age.get("title"))