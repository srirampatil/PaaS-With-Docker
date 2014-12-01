
"""
read-db.py: Query mysql database to check existence of a entry in the table

"""

import MySQLdb
import sys

repo_url = str(sys.argv[1]);
hostname = "localhost";
username = "root";
password = "iiit123";
database = "cloud_project";
table = "map";
column = "repo_url";


def mysql_connect():
	db = MySQLdb.connect(hostname, username, password, database);
	return db;

def create_cursor(db):
	cursor = db.cursor();
	return cursor;

def construct_query():
	query = "select * from %s where %s='%s'" %(table, column, repo_url);
	return query;

def execute_query(cursor, query):
	cursor.execute(query);
	return;

def print_result(cursor):
	rows = cursor.fetchall();
	print rows;

def check_result(cursor):
	if not cursor.rowcount:
	    print False;
        else:
	    print True;

def main():
	db =  mysql_connect();
	cursor = create_cursor(db);
 	query = construct_query();
	execute_query(cursor, query);
#print_result(cursor);
	check_result(cursor);
	return;

if __name__ == "__main__":
	main();
	


