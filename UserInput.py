# Daniel Bittner Aug 25, 2025
# First Program for InfoTech Capstone


nameInput = input("What is your name? ")
monthInput = input("What month were you born in? ")
print("Hello " + nameInput+ "!")

countName = len(nameInput)
print("Your name has " + str(countName) + " characters in it.")

from datetime import datetime

current_month_name = datetime.now().strftime("%B")
print(current_month_name)

print("Hello " + nameInput + "! You were born in " + monthInput + "")
if monthInput.lower() == current_month_name.lower():
    print("Happy birthday month!")

