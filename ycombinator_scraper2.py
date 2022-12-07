import requests
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/?p=3")
if response.status_code != 200:
	print("Error fetching page")
	exit()
else:
	content = response.content
#print(content)

soup = BeautifulSoup(response.content, 'html.parser')

def test_yolo(AAA, BBB):
	if(AAA.get("id") == BBB.span.get("id").split("score_")[1]):
		print("YES ----------- Id's are the same")
		print(str(first.find(class_="titleline").a.get("href")).replace("\n","")) # .get("href") .replace("\n","")
		print(str(first.find(class_="titleline").get_text()).replace("\n",""))
		print(first_b.span.get_text())
		print(first_b.find(class_="age").get("title"))
	else:
		print("NO")

all_at_athing = [a for a in soup.find_all(class_="athing")]
all_at_subline = [a for a in soup.find_all(class_="subline")]
all_at_things = [a for a in soup.find_all(class_="titleline")]  #  "athing"
all_subtext = [a for a in soup.find_all(class_="subtext")]
print(len(all_at_athing), len(all_at_subline), len(all_at_things), len(all_subtext))



# for a,b in zip(all_at_athing, all_at_subline):
# 	test_yolo(a, b)
# 	print("-------------- end --------")
first = all_at_athing[0]
first_b = all_at_subline[0]
#(title, link, points, date created)
print(first)

print(first_b)

print(first.get("id"))
print(first_b.span.get("id"))
if(first.get("id") == first_b.span.get("id").split("score_")[1]):
	print("YES ----------- Id's are the same")
	print(str(first.find(class_="titleline").a.get("href")).replace("\n","")) # .get("href") .replace("\n","")
	print(str(first.find(class_="titleline").get_text()).replace("\n",""))
	print(first_b.span.get_text())
	print(first_b.find(class_="age").get("title"))
else:
	print("NO")



# a = 0
# for i in all_at_athing:
# 	print(i.get("id"))
# 	a+=1
# print(a)

# b=0
# for i in all_at_subline:
# 	print(i.span.get("id")) # .find("id")
# 	b+=1
# print(b)

#----------------------------------------
# age_count = 0
# for thing in all_at_things:
# 	#print(thing)
# 	print(thing.a.get("href"))
# 	age_count+=1

# print(age_count)


# for thing in all_sublines:
#   print(thing)
# all_hrefs = [a for a in soup.find_all(class_="titleline")]
# print(len(all_hrefs))

# all_scores = [a for a in soup.find_all(class_="score")]
# print(len(all_scores))

# all_ages = [a for a in soup.find_all(class_="age")]
# print(len(all_ages))
#print(all_hrefs[0])
#print(all_hrefs[0].get_text())

# if(len(all_hrefs) == len(all_scores) and len(all_scores) == len(all_ages)):
#   print("-------------------YES--------------")
# else:
#   print("-------------------NO--------------")

# for href in all_hrefs:
#   print(href.a.get("href"))

# for href in all_hrefs:
#   print(href.get_text())

# for score in all_scores:
#   print(score.get_text())

# for age in all_ages:
#   print(age.get("title"))

