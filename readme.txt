1. Installation:
	Install following packages:
	1. MySQL - "sudo apt-get install mysql-server"
	2. Python mysql binding - "sudo apt-get install python-mysqldb"

2. Configuration:
	1. Modify the hostname, username, databasenamse, password, tablename, columnsname
           in "update-db.py" and "read-db.py" file. 
 	   This is not necessary step, but if you are willing to change the database name please make
           correspoding changes in programs also.

3. Functions
Program1: update-db.py
- *Signature:* update-db:: repo-url, image-id
- *Input parameters:* repo-url and image-id 
- *Input Type:* string, string
- *Funtionality:* Insert an entry (repo-url, image-id) in the database
- *Return parameters:* True or False
- *Return Type:* Boolean

Program2: read-db.py
- *Signature:* read-from-db:: repo-url
- *Input parameters:* repo-url
- *Input Type:* string
- *Functionality:* Searches for an entry in the database
- *Return parameters:* True or False
- *Return Type:* Boolean

Program3: init.py
- *Signature:* init-db::
- *Input parameters:* datababase-name, table-name, column1-name, column2-name
- *Input Type:* string
- *Functionality:* Initializes a datababase and creates a table
- *Returns:* Nothing





