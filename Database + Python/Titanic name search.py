import sqlite3

#Conditions
ask = True
keep_ask = True

#Importing database
DATABASE = "../DB Browser/titanic.db"

#Connecting database
connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

print("Welcome to the Titanic passengers database")
print("="*40)
print("Here you can search for passengers and their details")

name = input("Enter the name: ")
cursor.execute("SELECT COUNT(passenger_id) FROM titanic WHERE name = ?", (name,))
results = cursor.fetchall()
print(f"{results[0]} 8 result(s) found")
cursor.execute("SELECT fare, name, class, age FROM titanic WHERE name = ?", (name,))
results = cursor.fetchall()
print(f"{'Name':15} {'Class':5} {'Age':5} {'Fare':10}")
for i in results:
    print(f"{i[0]:10} {i[1]:10}")


