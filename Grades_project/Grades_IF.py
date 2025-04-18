grade = int(input("Enter your grade: "))
if grade <= 100 and grade >= 90:
    print("You got A, Excellent")
elif grade >= 80:
    print("You got B, Very Good")
elif grade >= 70:
    print("You got C, Good")
elif grade >= 60:
    print("You got D, Needs Improvement")
elif grade >= 0:
    print("You got F, Failed")
else:
    print("Invalid grade entered.")
