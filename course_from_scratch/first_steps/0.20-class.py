class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(self.first_name, self.last_name, self.age)

    def is_male(self):
        return self.first_name [1:] != 'a'

user = User("John", "Smith", "25")
user.describe_user()
print(user.is_male())