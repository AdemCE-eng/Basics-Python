grade = int(input("Enter your grade: "))
match grade:
    case g if 90 <= g <= 100:
        print("You got A, Excellent")
    case g if 80 <= g < 90:
        print("You got B, Very Good")
    case g if 70 <= g < 80:
        print("You got C, Good")
    case g if 60 <= g < 70:
        print("You got D, Needs Improvement")
    case g if 0 <= g < 60:
        print("You got F, Failed")
    case _:
        print("Invalid grade entered.")