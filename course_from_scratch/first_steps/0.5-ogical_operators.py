a = 5
b = 2

# print(a > b and b > 0)
# print(a > b and b > 3)
# print(a > 10 or (b > 0 and a < b))

c = 5

print(c % 2 == 0)
# zwraca true dla liczb parzystych
# zwraca false dla liczb nieparzystych

print(not c % 2 == 0)
# zwraca false dla liczb parzystych
# zwraca true dla liczb nieparzystych

user_logged_in = False

if user_logged_in:
    print("user logged in")

if not user_logged_in:
    print("user not logged in")