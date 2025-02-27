# def hello(name, age, last_name=None):
#     print("hello " + name + "! and " + str(age) + " Lat")
#     if last_name is not None:
#         print("my last name is " + last_name)
#
#
# hello("Jakub",26, 'Marcinkowski')
# # hello("Piotr", 23)
# # hello("Marta", 20)

# def strip_and_uppercase(text):
#     return text.strip().upper()
#
# text = strip_and_uppercase("jestem jakub I lubie programować")
# print(text)



countries_information = {}
countries_information ['Polska'] = ('Warszawa', 38)
countries_information ['Niemcy'] = ('Berlin', 83)
countries_information ['Switzerland'] = ('Switzerland', 54)

country = 'Niemcy'
def print_country_information(country):
    print('Countries : ' + country)
    print('capital : ' + countries_information[country][0])
    print('number of inhabitants : ' + str(countries_information[country][1]) + 'million')

print_country_information('Niemcy')

print()

print_country_information('Switzerland')

print()

print_country_information('Polska')