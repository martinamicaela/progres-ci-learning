import psycopg2
# conect to "chinook" database
connection= psycopg2.connect(database="chinook")


# build a cursor object of the database 
cursor= connection.cursor()
# Query 1 select all records from "artist" table 
cursor.execute('SELECT * FROM "artist"')

#fetch the results (multiple)
results=cursor.fetchall()
#fetch the results (single)
#results=connection.fetchone()

#close the connection 
connection.close()

# print results 
for result in results:
    print(result)