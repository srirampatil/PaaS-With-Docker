
"""
init.py: Initializes environment by creating a database and a table;
         This script should be run only once at the starting of the setup.

"""

import MySQLdb
import sys

hostname = "localhost";
username = "root";
password = "iiit123";
database = "testdb";
table = "map";
column1 = "repo_url";
column2 = "image_id";


def mysql_connect():
	db = MySQLdb.connect(hostname, username, password);
	return db;

def create_cursor(db):
	cursor = db.cursor();
	return cursor;

def construct_query(option):
	if option == 1:
		query = "create database %s" %(database);
	elif option == 2:
		query = "use %s" %(database);
	elif option == 3:
		query = "create table %s (%s varchar(255), %s varchar(255))" %(table, column1, column2);
	return query;


def execute_query(cursor, query):
	cursor.execute(query);
	return;

def main():
	db =  mysql_connect();
	cursor = create_cursor(db);

	# Create a Database
 	query = construct_query(1);
	execute_query(cursor, query);

 	#Use the Database
	query = construct_query(2);
	execute_query(cursor, query);

	#Create a table
	query = construct_query(3);
	execute_query(cursor, query);

	return;

if __name__ == "__main__":
	main();
	
