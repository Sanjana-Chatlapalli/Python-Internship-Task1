# This program prints intern details
# Taking user input

name = input("Enter your name: ")
role = input("Enter your internship role: ")

from datetime import date
today = date.today()

# Printing output
print("\n--- Intern Details ---")
print("Name:", name)
print("Role:", role)
print("Date:", today)