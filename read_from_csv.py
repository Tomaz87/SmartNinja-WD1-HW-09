import csv

print("Hello! This program reads users data from csv and show them in the sentences.")

with open("user_list.csv") as users_introduction:
    reader = csv.DictReader(users_introduction)

    for row in reader:
        print(row["Name"] + " is " + row["Gender"] + " and is " + row["Age"] + " years old.")
