'''Example of connecting to a database and running queries'''

###This is the setup stuff that will appear on every program###

#Start by importing the sqlite3 library
import sqlite3

#Set the database that we will connect to
#This is uppercase as it is a constant (won't change during the program)
#Make sure this file is saved in the same folder as the database
DATABASE = "DB Browser/cars.db"

#Connect database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

#Run a query
cursor.execute("SELECT plate, make, model FROM car")
#Get results
results = cursor.fetchall()

#Loop over results list and display each result one at a time
print(f"{'Number Plate':13} {'Make':14} Model")
print("="*38)
for student in results:
    print(f"{student[0]:13} {student[1]:14} {student[2]}")

