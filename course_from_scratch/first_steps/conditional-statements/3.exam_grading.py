exam = int(input("Whot is you Exam result? Enter from 0-100 : "))

if exam <= 50:
    print("you rating is 2")
elif exam >= 51 and exam <= 69:
    print ("your rating is 3")
elif exam >= 70 and exam <= 80:
    print("your rating is 4")
elif exam >= 81 and exam <= 89:
    print("your rating is 5")
elif exam >= 90 and exam <= 100:
    print("your rating is 6")
else:
    print("there are no other results")