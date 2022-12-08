import requests
from bs4 import BeautifulSoup
import pypyodbc as data_handler
import sys

response = requests.get("https://news.ycombinator.com/") # https://news.ycombinator.com/?p=3
if response.status_code != 200:
	print("Error fetching page")
	exit()
else:
	content = response.content
#print(content)

soup = BeautifulSoup(response.content, 'html.parser')
#"""
# def test_yolo(AAA, BBB):
# 	if(AAA.get("id") == BBB.span.get("id").split("score_")[1]):
# 		#print("YES ----------- Id's are the same")
# 		print(str(AAA.find(class_="titleline").a.get_text()).replace("\n","")) 
# 		print(add_link(str(AAA.find(class_="titleline").a.get("href")).replace("\n",""))) 
# 		print(int(BBB.span.get_text().split(" ")[0]))
# 		print(BBB.find(class_="age").get("title").replace("T", " "))
# 	else:
# 		print("NO")

def add_link(the_link):
	if(the_link.startswith("item")):
		return "https://news.ycombinator.com/" + the_link
	return the_link

all_at_athing = [a for a in soup.find_all(class_="athing")]
all_at_subline = [a for a in soup.find_all(class_="subline")]
#all_at_things = [a for a in soup.find_all(class_="titleline")]  #  "athing"
#all_subtext = [a for a in soup.find_all(class_="subtext")]
print(len(all_at_athing), len(all_at_subline)) # , len(all_at_things), len(all_subtext)



# for a,b in zip(all_at_athing, all_at_subline):
# 	test_yolo(a, b)
# 	print("-------------- end --------")
first = all_at_athing[0]
first_b = all_at_subline[0]
#(title, link, points, date created)
# print(first)

# print(first_b)

# print(first.get("id"))
# print(first_b.span.get("id"))
# if(first.get("id") == first_b.span.get("id").split("score_")[1]):
# 	print("YES ----------- Id's are the same")
# 	print(str(first.find(class_="titleline").a.get_text()).replace("\n","")) 
# 	print(add_link(str(first.find(class_="titleline").a.get("href")).replace("\n",""))) 
# 	print(int(first_b.span.get_text().split(" ")[0]))
# 	print(first_b.find(class_="age").get("title").replace("T", " "))
# else:
# 	print("NO")
#"""
big_2d_list = []

def create_2d_list(titleAndLink, pointsAndDate):
	temporary_list = []
	for t_and_l, p_and_d in zip(titleAndLink, pointsAndDate):
		appendable_list = append_to_list(t_and_l, p_and_d, temporary_list)
		if(len(appendable_list) > 0):
			big_2d_list.append(appendable_list)
		else:
			print("No append")
	return 1

def append_to_list(titleAndLink, pointsAndDate, tempListToAppend):
	if(titleAndLink.get("id") == pointsAndDate.span.get("id").split("score_")[1]):
		#print("YES ----------- Id's are the same")
		the_id = int(titleAndLink.get("id"))
		the_title = str(titleAndLink.find(class_="titleline").a.get_text()).replace("\n","")
		the_link = add_link(str(titleAndLink.find(class_="titleline").a.get("href")).replace("\n",""))
		the_points = int(pointsAndDate.span.get_text().split(" ")[0])
		the_date_created = str(pointsAndDate.find(class_="age").get("title").replace("T", " ")).replace("\n","")
		tempListToAppend = [the_id, the_title, the_link, the_points, the_date_created]
		# print(str(AAA.find(class_="titleline").a.get_text()).replace("\n","")) 
		# print(add_link(str(AAA.find(class_="titleline").a.get("href")).replace("\n",""))) 
		# print(int(BBB.span.get_text().split(" ")[0]))
		# print(BBB.find(class_="age").get("title").replace("T", " "))
	else:
		print("NO")

	return tempListToAppend

create_2d_list(all_at_athing, all_at_subline)





# for mini_list in big_2d_list:
# 	print(mini_list)
#---------ADD TO DATABSE ------------- 
def insert_data_to_database():
	test_list = [
		[12312, "test title 1", "https://test.link.com", 10, "2021-11-07 17:56:16"],
		[12344, "test title 2", "https://test.link.com", 20, "2022-12-07 17:56:16"]
		]

	DRIVER = "SQL Server"
	SERVER_NAME = "DESKTOP-P3PDNDA"
	DATABASE_NAME = "y-combinator"

	conn_string = f"""
		Driver={{{DRIVER}}};
		Server={SERVER_NAME};
		Database={DATABASE_NAME};
		Trust_connection=yes;
	"""

	try:
		conn = data_handler.connect(conn_string)
	except Exception as e:
		print(e)
		print("Connection failed")
		sys.exit()
	else:
		cursor = conn.cursor()

	insert_statement = """
		INSERT INTO scraped_data
		VALUES (?, ?, ?, ?, ?)
	"""

	try:
		for record in big_2d_list: # test_list # big_2d_list
			print(record)
			cursor.execute(insert_statement, record)
	except Exception as e:
		cursor.rollback()
		print(e.value)
		print("Transaction failed = rollback")
	else:
		print("Records inserted successfully")
		cursor.commit()
		cursor.close()
	finally:
		if conn.connected == 1:
			print("Connection closed successfully")
			conn.close()
# end uf inser data base

def update_database():
	DRIVER = "SQL Server"
	SERVER_NAME = "DESKTOP-P3PDNDA"
	DATABASE_NAME = "y-combinator"

	conn_string = f"""
		Driver={{{DRIVER}}};
		Server={SERVER_NAME};
		Database={DATABASE_NAME};
		Trust_connection=yes;
	"""

	try:
		conn = data_handler.connect(conn_string)
	except Exception as e:
		print(e)
		print("Connection failed")
		sys.exit()
	else:
		cursor = conn.cursor()

	insert_statement = """
		INSERT INTO scraped_data
		VALUES (?, ?, ?, ?, ?)
	"""
	update_statement = """
		UPDATE scraped_data SET points = 'Canyon 123' WHERE address = 'Valley 345'
	"""

	try:
		for record in big_2d_list: # test_list # big_2d_list
			print(record)
			# [the_id, title, link, points, "2021-11-07 17:56:16"],
			cursor.execute(f"""
				UPDATE scraped_data SET points = {record[3]} WHERE the_id = {record[0]}
				""") # , record
	except Exception as e:
		cursor.rollback()
		print(e.value)
		print("Transaction failed = rollback")
	else:
		print("Records updated successfully")
		cursor.commit()
		cursor.close()
	finally:
		if conn.connected == 1:
			print("Connection closed successfully")
			conn.close()


	return ":)"

# call insert
#insert_data_to_database()
# CALL UPDATE FUNCTION!!!!
update_database()

# END OF ADDING TO DATABSE -----------------------
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

