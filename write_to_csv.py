import csv

print("Hello! This program collects users data and store them in the csv file.")

print("Fill in required data below please.")
name = input(f"First name: ").capitalize()
age = int(input("Age: "))
gender = input(f"Gender: ").lower()

with open("user_list.csv", "a") as list_of_users:
    list_of_users.write(f'{name},{age},{gender}'"\n")
