'''Searching the cars database'''

import sqlite3

DATABASE = "../DB Browser/cars.db"

connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

##### Get plate from user and run search #####
plate = input("Enter plate number: ")

# This search requires an exact much
cursor.execute("SELECT plate, owner FROM car WHERE plate = ?", (plate,))
results = cursor.fetchall()

for car in results:
    print(f"{car[0] : 10} {car[1] : 10}")

#Fuzzy search, looks for plates that INCLUDE the variable
like_plate = f"%{plate}%"
cursor.execute("SELECT plate, owner FROM car WHERE plate LIKE ?", (like_plate,))

results = cursor.fetchall()
for car in results:
    print(f"{car[0]:10} {car[1]:10}")


name = input("Name: ")
model = input("Model: ")
cursor.execute("SELECT plate, owner, FROM car WHERE owner = ? and model = ?", (name, model))
result = cursor.fetchall()

for car in results:
    print(f"{car[0]:10} {car[1]:10}")
