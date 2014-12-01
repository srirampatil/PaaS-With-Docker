
"""
update-db.py: Insert an entry in mysql database

"""

import MySQLdb
import sys

hostname = "localhost";
username = "root";
password = "iiit123";
database = "cloud_project";
table = "map";
repo_url = str(sys.argv[1]);
image_id = str(sys.argv[2]);


def mysql_connect():
	db = MySQLdb.connect(hostname, username, password, database);
	return db;

def create_cursor(db):
	cursor = db.cursor();
	return cursor;

def construct_query():
	query = "insert into %s values('%s','%s')" %(table, repo_url, image_id);
	return query;

def execute_query(db, cursor, query):
	cursor.execute(query);
	db.commit()
	return

def main():
	db =  mysql_connect();
	cursor = create_cursor(db);
 	query = construct_query();
	return execute_query(db, cursor, query);

if __name__ == "__main__":
	main();
	
