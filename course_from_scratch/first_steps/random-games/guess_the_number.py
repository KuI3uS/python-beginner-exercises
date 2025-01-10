import random
i = random.randint(0,100)


while True:
    numer = int(input("Enter a number: "))
    if numer < i:
        print("your the number is too small" )
    elif numer > i:
        print("your the number is too big" )
    else:
        print("you guessed the number")
        break

