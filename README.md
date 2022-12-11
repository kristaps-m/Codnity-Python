### Download

Microsoft SQL Server Management Studio
https://learn.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver16

SQL Server
https://www.microsoft.com/en-us/sql-server/sql-server-downloads

Python
https://www.python.org/downloads/

.NET 6.0
https://dotnet.microsoft.com/en-us/download

Create new database named 'y-combinator'
Create new Table in Microsoft SQL Server Management Studio 'scraped_data'

<table>
  <tr>
    <th>Example</th>
    <th>Picture</th>    
  </tr>
  <tr>
    <td>

	the_id : int,
	title : nvarchar(MAX),
	link : nvarchar(MAX),
	points : int,
	created_date : datetime
</td>
    <td><img src="pictures/create_table.png" alt="create_table.png"></td>    
  </tr>
</table>


Go to <br>
...\codnity_python
open cmd or powershell type 'python ycombinator_scraper.py'

Go to <br>
...\codnity_python\UserInterface\react-ui
open cmd or powershell type 'npm install' and then 'npm start'

Go To <br>
...\codnity_python\API\ycombinator\ycombinator
open cmd or powershell type 'dotnet watch run'

Go To <br>
https://localhost:7191/swagger/index.html
And you can test C# backend

Go To <br>
http://localhost:3000
To see front end example