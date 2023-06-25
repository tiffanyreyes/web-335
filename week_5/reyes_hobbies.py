
#===========================================================================================
#; Title: reyes-hobbies.py
#; Author: Tiffany Reyes
#; Date: 21 June 2023
#; Description: Python conditionals, lists, and loops
#;==========================================================================================

# Variables of different hobbies
hobbies = ["reading", "singing", "drawing", "working out", "playing video games"]
# For loop for displaying hobbies
for hobby in hobbies:
    print(hobby)

# Variables of the different days of the week
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
# For loop for displaying days for hobbies or work
for day in days:
    if day == "Sunday" or day == "Saturday":
        print(f"Today is {day}. Go and enjoy your hobbies!")
    else:
        print(f"Today is {day}. It is a work day.")     