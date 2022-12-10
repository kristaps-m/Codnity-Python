
Creating C# backend and React F.E.
https://www.youtube.com/watch?v=ON-Z1iD6Y-c
19:20 adds method to add something to table, but we don't need that!
23:50 Adds another controller
36:24 Creates Variables.js
38:32 manipulates table
56:00 Starts to add filtering
5?:00 Starts to add sorting

paginator !
https://www.youtube.com/watch?v=IYCa1F-OWmk


Trusted connection
https://stackoverflow.com/questions/8075784/error-message-provider-shared-memory-provider-error-0-no-process-is-on-th


f"""
insert into [y-combinator].[dbo].[scraped_data] ([the_id]
,[title]
,[link]
,[points]
,[date_created])
select _ from (
values ({record[0]}, '{record[1].replace("'", "")}', '{record[2]}', {record[3]}, '{record[4]}') -- sample value
) as s([the_id]
,[title]
,[link]
,[points]
,[date_created])
where not exists (
select _ from [y-combinator].[dbo].[scraped_data] t with (updlock)
where s.[the_id] = t.[the_id]
)
"""

#-------------------

f"""
insert into [y-combinator].[dbo].[scraped_data] ([the_id]
,[title]
,[link]
,[points]
,[date_created])
select _ from (
values ({record[0]}, '{record[1]}', '{record[2]}', {record[3]}, '{record[4]}') -- sample value
) as s([the_id]
,[title]
,[link]
,[points]
,[date_created])
where not exists (
select _ from [y-combinator].[dbo].[scraped_data] t with (updlock)
where s.[the_id] = t.[the_id]
)
"""

#-------------------
f"""
insert into scraped*data (the_id
,title
,link
,points
,date_created)
select * from (
values ({record[0]}, '{record[1]}', '{record[2]}', {record[3]}, '{record[4]}')
)
where not exists (
select \_ from scraped_data t with (updlock)
where scraped_data.the_id = t.the_id
)
"""
#------------------------------------------------
f"""
SELECT \* FROM scraped_data

    			if not exists (SELECT * FROM scraped_data WHERE the_id = {record[0]})

    			BEGIN
    				INSERT INTO scraped_data (the_id, title, link, points, date_created)
    				VALUES ({record[0]}, '{record[1].replace("'","")}', '{record[2]}', {record[3]}, '{record[4]}')
    			END
    		"""
