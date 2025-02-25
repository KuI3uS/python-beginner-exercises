def hello(name, age, last_name=None):
    print("hello " + name + "! and " + str(age) + " Lat")
    if last_name is not None:
        print("my last name is " + last_name)


hello("Jakub",26, 'Marcinkowski')
# hello("Piotr", 23)
# hello("Marta", 20)