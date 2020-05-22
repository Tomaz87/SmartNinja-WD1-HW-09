import csv

with open("user_list.csv") as users_introduction:
    reader = csv.DictReader(users_introduction)

    for row in reader:
        print(row["Name"] + " is " + row["Gender"] + " and is " + row["Age"] + " years old.")