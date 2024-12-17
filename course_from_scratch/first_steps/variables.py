name = input("What is your name?")
age = input("What is your age ?")

print("hello " + name + "! " + " your age is: " + age)

if int(age) <= 17:
    print("You are a minor")
else:
    print("you are an adult")