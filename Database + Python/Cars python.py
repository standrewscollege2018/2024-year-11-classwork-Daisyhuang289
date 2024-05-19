import sqlite3

DATABASE = "DB Browser/cars.db"

connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

cursor.execute("SELECT plate, make, model FROM car")
results = cursor.fetchall()

print(f"{'Number Plate':10} {'Make':15} Model")
print("="*38)
for car in results:
    print(f"{car[0]:10} {car[1]:15} {car[2]}")
