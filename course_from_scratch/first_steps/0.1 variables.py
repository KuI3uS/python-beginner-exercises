name = input("What is your name ?")
lastName = input("what is your last name ?")
old = input("what old are you ?")

print("hello : " + name + "\nlast name : " + lastName + "\nyour old : " + old)

if int(old) <= 17:
    print("you are a minor")
else:
    print("you are of legal age")