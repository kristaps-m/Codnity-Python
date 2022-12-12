import requests
from bs4 import BeautifulSoup
import pypyodbc as data_handler
import sys
# For printing with colors
import os
os.system('cls')

"""VARIABLES"""
big_2d_list = []
how_many_pages_from_site = 0
DRIVER = "SQL Server"
SERVER_NAME = "." # DESKTOP-P3PDNDA
DATABASE_NAME = "y-combinator"

"""
How it Works?
Step 1: Ask user for a integer. To find out how many 'news.ycombinator.com/?p={1-n}' pages need to be scraped!
Step 2: Integer from Step 1 is put in get_more_than_one_page() function and data from site is scraped and put in two lists.
Step 3: Function create_2d_list() is beeing called. Two list from step 2 is passed in.
Step 4: Function create_2d_list() and append_to_list_with_id_check is being called and creates 2 dimensional list.
Step 5: User can choose 'input' or 'update' data base!
"""

# Step 1
print("Welcome to the 'news.ycombinator.com/' web scraper")
while True:
  user_pages_input = input("How many pages you want to scrape?\nEnter: ")
  if(user_pages_input.isdigit()):
    user_pages_input = int(user_pages_input)
  else:
    print("Please enter an integer")

  if(user_pages_input < 1):
    user_pages_input = 1
  how_many_pages_from_site = user_pages_input
  break

# Step 2
def get_more_than_one_page(how_many):
  big_all_at_athing = []
  big_all_at_subline = []
  for i in range(1, how_many + 1):    
    response = requests.get(f"https://news.ycombinator.com/?p={i}")
    if response.status_code != 200:
      print("Error fetching page")
      exit()
    else:
      content = response.content
    soup = BeautifulSoup(response.content, 'html.parser')
    all_at_athing_local = [a for a in soup.find_all(class_="athing")]
    all_at_subline_local = [a for a in soup.find_all(class_="subline")]
    print(f"Getting data from page: 'https://news.ycombinator.com/?p={i}'")
    for titleAndLink in all_at_athing_local:
      #print("Comparring Id's prepering data ....!")
      for pointsAndDate in  all_at_subline_local:
        if(titleAndLink.get("id") == pointsAndDate.span.get("id").split("score_")[1]):          
          #print(titleAndLink.get("id"), pointsAndDate.span.get("id").split("score_")[1])
          big_all_at_athing.append(titleAndLink)
          big_all_at_subline.append(pointsAndDate)
          break
  print("All data found!")        
  return [big_all_at_athing, big_all_at_subline]

def add_link(the_link):
  if(the_link.startswith("item")):
    return "https://news.ycombinator.com/" + the_link
  return the_link

# Step 2
all_at_athing = get_more_than_one_page(how_many_pages_from_site)[0]
all_at_subline = get_more_than_one_page(how_many_pages_from_site)[1]
print("Data scraped and prepered!")

# Step 4
def create_2d_list(titleAndLink, pointsAndDate):
  temporary_list = []
  for t_and_l, p_and_d in zip(titleAndLink, pointsAndDate):
    appendable_list = append_to_list_with_id_check(t_and_l, p_and_d, temporary_list)
    
    if(len(appendable_list) > 0):
      big_2d_list.append(appendable_list)
    else:
      print("No append")

# Step 4
def append_to_list_with_id_check(titleAndLink, pointsAndDate, tempListToAppend):
  if(titleAndLink.get("id") == pointsAndDate.span.get("id").split("score_")[1]):
    #print("YES ----------- Id's are the same")
    the_id = int(titleAndLink.get("id"))
    the_title = str(titleAndLink.find(class_="titleline").a.get_text()).replace("\n","")
    the_link = add_link(str(titleAndLink.find(class_="titleline").a.get("href")).replace("\n",""))
    the_points = int(pointsAndDate.span.get_text().split(" ")[0])
    the_date_created = str(pointsAndDate.find(class_="age").get("title").replace("T", " ")).replace("\n","")
    tempListToAppend = [the_id, the_title, the_link, the_points, the_date_created]
  else:
    the_id = int(titleAndLink.get("id"))
    the_second_id = pointsAndDate.span.get("id").split("score_")[1]
    print(f"NO -------- {the_id} and {the_second_id}")

  return tempListToAppend

# Step 3
create_2d_list(all_at_athing, all_at_subline)

#Step 5:
def insert_data_to_database():
  test_list = [
    [12312, "test title 1", "https://test.link.com", 10, "2021-11-07 17:56:16"],
    [12344, "test title 2", "https://test.link.com", 20, "2022-12-07 17:56:16"]
    ]

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
    for record in big_2d_list: 
      print(record)
      # [the_id, title, link, points, date_created],
      cursor.execute(f"""
      insert into scraped_data (the_id, title, link, points, date_created)
      select * from (
      values ({record[0]}, '{record[1].replace("'", "")}', '{record[2]}', {record[3]}, '{record[4]}') -- insert values
      ) as s(the_id, title, link, points, date_created)
      where not exists (
      select * from scraped_data t with (updlock)
      where s.the_id = t.the_id
      )
      """) # insert_statement, record
  except Exception as e:
    cursor.rollback()
    print(e.value)
    print("\u001b[31;1m  Transaction failed = rollback\u001b[0m")
  else:
    print("\u001b[32;1m  Records inserted successfully")
    cursor.commit()
    cursor.close()
  finally:
    if conn.connected == 1:
      print("  Connection closed successfully\u001b[0m")
      conn.close()
# end of inser data base function

#Step 5:
def update_database():
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

  try:
    for record in big_2d_list: 
      print(record)
      cursor.execute(f"""
        UPDATE scraped_data SET points = {record[3]} WHERE the_id = {record[0]}
        """)
  except Exception as e:
    cursor.rollback()
    print(e.value)
    print("\u001b[31;1m  Transaction failed = rollback\u001b[0m")
  else:
    print("\u001b[32;1m  Records updated successfully")
    cursor.commit()
    cursor.close()
  finally:
    if conn.connected == 1:
      print("  Connection closed successfully\u001b[0m")
      conn.close()
# end of update data function!

#Step 5:
while True:  
  user_scrape_or_update_input = input("Enter 'import' or 'update'\nEnter: ")
  
  if(user_scrape_or_update_input.lower() == "import"):      
    print(f"Inserting data from {user_pages_input} pages")
    print("Inserting....")
    # CALL INSERT FUNCTION!!!!
    insert_data_to_database()
  elif (user_scrape_or_update_input == "update"):
    print("Updating....")
    # CALL UPDATE FUNCTION!!!!
    update_database()
  else:
    print("Invalid input")
  break
