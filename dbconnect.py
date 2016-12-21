import datetime
import psycopg2

def tryConnect():
	try:
	    conn = psycopg2.connect("dbname='website' user='cyoth' host='localhost' password='defruThegE1'")
	except:
	    print("I am unable to connect to the database")

	return conn

def insertUser(db, username, firstname, lastname, email, password):
	sqlquery = ("INSERT INTO website01.users (user_nm,user_first_name,user_last_name,user_email,password_txt) VALUES ('%s','%s','%s','%s','%s')" % (username,firstname,lastname,email,password))
	try:
	    conn = psycopg2.connect("dbname='website' user='cyoth' host='localhost' password='defruThegE1'")
	except:
	    print("I am unable to connect to the database")

	cur = conn.cursor()

	try:
		cur.execute(sqlquery)
	except:
		print("INSERT INTO website01.users (user_nm,user_first_name,user_last_name,user_email,password_txt) VALUES ('%s','%s','%s','%s','%s')" % (username,firstname,lastname,email,password))
		print("I can't drop our test database!")	
	conn.commit()