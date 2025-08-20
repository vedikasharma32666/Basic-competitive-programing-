#15. Accept the percentage from the user and display the grade according to the following criteria.
percentage = int(input("Enter your percentage: "))

if percentage >= 90 and percentage <= 100:
    print("Grade: A")
elif percentage >= 80:
    print("Grade: B")
elif percentage >= 70:
    print("Grade: C")
elif percentage >= 60:
    print("Grade: D")
elif percentage >= 0:
    print("Grade: F")
else:
    print("Invalid percentage.  enter a value between 0 and 100.")
    



